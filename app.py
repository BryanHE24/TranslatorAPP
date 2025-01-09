from flask import Flask, render_template, request
import requests
import uuid
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Flask app setup
app = Flask(__name__)

# Load Azure Translator API settings from .env
KEY = os.getenv('KEY')
ENDPOINT = os.getenv('ENDPOINT')
LOCATION = os.getenv('LOCATION')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        original_text = request.form.get('text')
        target_language = request.form.get('language')

        # Build Azure Translator API request
        path = '/translate?api-version=3.0'
        target_language_parameter = "&to=" + target_language
        constructed_url = ENDPOINT + path + target_language_parameter

        # API headers
        headers = {
            'Ocp-Apim-Subscription-Key': KEY,
            'Ocp-Apim-Subscription-Region': LOCATION,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # API request body
        body = [{'text': original_text}]

        # Make API call
        try:
            translator_request = requests.post(constructed_url, headers=headers, json=body)
            translator_request.raise_for_status()
            translator_response = translator_request.json()

            # Extract translated text
            translated_text = translator_response[0]['translations'][0]['text']

            # Pass the result to the template
            return render_template(
                'results.html',
                original_text=original_text,
                translated_text=translated_text,
                target_language=target_language
            )
        except Exception as e:
            return f"An error occurred: {e}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
