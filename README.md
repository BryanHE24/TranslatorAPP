# Azure Translator Flask App

## Overview
This project is a web application built with Flask that allows users to translate text into various languages using the Azure Translator API. It is designed with a clean user interface powered by Bootstrap and ensures secure handling of API credentials through a `.env` file.

## Features
- Text input for the user to enter text to be translated.
- Dropdown to select the target language.
- Integration with Azure Translator API for real-time translation.
- Secure handling of API keys using `python-dotenv`.

## Folder Structure
```
TranslatorWebAPP_Azure/
├── templates/                # HTML templates for the Flask app
│   ├── index.html           # Input form for text and language selection
│   └── results.html         # Displays translation results
├── app.py                   # Main application logic
├── .env                     # Environment variables (not committed to Git)
├── .env.example             # Example environment file for setup
├── requirements.txt         # Python dependencies
└── .gitignore              # Files to ignore in Git
```

## Installation and Usage

### Prerequisites
- Python 3.9 or higher
- Azure Translator API key and endpoint
- Basic knowledge of Flask and Azure services

### Steps to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/BryanHE24/TranslatorAPP.git
   cd TranslatorWebAPP_Azure
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a translator resource and then Set up your .env file like this:
   ```bash
   KEY=yourazureresourcekey
   LOCATION=yourregion
   ENDPOINT=yourendpoint
   ```

5. Run the Flask App:
   ```bash
   python app.py
   ```
   The app will be accessible at http://127.0.0.1:5000.

6. Enter text, select a target language (Language code example: es, en, fr), and view the translation
