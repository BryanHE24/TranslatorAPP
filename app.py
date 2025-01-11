import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key and endpoint from environment variables
TRANSLATOR_KEY = os.getenv("KEY")
TRANSLATOR_ENDPOINT = os.getenv("ENDPOINT")
TRANSLATOR_REGION = os.getenv("LOCATION")

# Initialize Flask app
app = Flask(__name__)

# Route to display the translation form and results
@app.route("/", methods=["GET", "POST"])
def translate():
    original_text = ""
    translated_text = ""
    if request.method == "POST":
        # Get text and selected language from the form
        original_text = request.form["text"]
        target_language = request.form["language"]

        # Call Azure Translator API to get the translation
        translated_text = get_translation(original_text, target_language)

    # Render the page with the original and translated text
    return render_template("index.html", original_text=original_text, translated_text=translated_text)

def get_translation(text, target_language):
    """Function to call Azure Translator API and get the translation"""
    # Construct the request URL
    url = f"{TRANSLATOR_ENDPOINT}/translate?api-version=3.0&to={target_language}"

    # Prepare the headers for the request
    headers = {
        "Ocp-Apim-Subscription-Key": TRANSLATOR_KEY,
        "Ocp-Apim-Subscription-Region": TRANSLATOR_REGION,
        "Content-Type": "application/json"
    }

    # Prepare the request body
    body = [{
        "text": text
    }]

    # Send POST request to the Azure Translator API
    response = requests.post(url, headers=headers, json=body)

    # Check if the request was successful
    if response.status_code == 200:
        translation = response.json()[0]["translations"][0]["text"]
        return translation
    else:
        # Handle error if translation failed
        return "Error: Could not translate text."

# Route to get supported languages from Azure Translator API
@app.route("/languages", methods=["GET"])
def get_languages():
    """Fetch supported languages from Azure Translator API"""
    url = f"{TRANSLATOR_ENDPOINT}/languages?api-version=3.0"

    headers = {
        "Ocp-Apim-Subscription-Key": TRANSLATOR_KEY,
        "Ocp-Apim-Subscription-Region": TRANSLATOR_REGION,
        "Content-Type": "application/json"
    }

    # Send GET request to the API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        languages = response.json()["translation"]
        # Return the language codes
        return jsonify(languages)
    else:
        return jsonify({"error": "Failed to fetch languages."}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
