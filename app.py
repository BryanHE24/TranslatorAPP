from flask import Flask, render_template, request, redirect, url_for
import os
import requests
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Get API key and endpoint from environment variables
TRANSLATOR_KEY = os.getenv("KEY")
TRANSLATOR_ENDPOINT = os.getenv("ENDPOINT")
TRANSLATOR_REGION = os.getenv("LOCATION")

@app.route("/", methods=["GET", "POST"])
def translate():
    translated_text = ""
    if request.method == "POST":
        text = request.form.get("text")
        language = request.form.get("language")
        translated_text = get_translation(text, language)
    return render_template("index.html", translated_text=translated_text)

def get_translation(text: str, target_language: str):
    """Function to call Azure Translator API and get the translation"""
    url = f"{TRANSLATOR_ENDPOINT}/translate?api-version=3.0&to={target_language}"

    headers = {
        "Ocp-Apim-Subscription-Key": TRANSLATOR_KEY,
        "Ocp-Apim-Subscription-Region": TRANSLATOR_REGION,
        "Content-Type": "application/json"
    }

    body = [{"text": text}]

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        return response.json()[0]["translations"][0]["text"]
    else:
        return "Error: Could not translate text."

if __name__ == "__main__":
    app.run(debug=True)
