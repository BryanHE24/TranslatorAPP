# Elegant Translator

A simple yet elegant web application for text translation, leveraging the Azure Translator API. This project provides a user-friendly interface for translating text between multiple languages, along with text-to-speech and voice input capabilities.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)

## Features
*   **Text Translation**: Translate text between multiple languages using the Azure Translator API.
*   **Text-to-Speech**: Listen to the translated text with the browser's built-in text-to-speech capability.
*   **Voice Input:** Input text by speaking using browser's speech recognition functionality.
*   **Elegant UI:**  A minimalist and user-friendly interface with a clean design, inspired by modern aesthetics.
*  **Responsive Design:** Adapts to various screen sizes from large Desktop down to Small Mobiles providing a smooth user experience.
## Technologies Used

### Frontend
*   **HTML:** Provides the structure of the web application using HTML5 .
*   **CSS:** Styles the web application with CSS3, using variables for a better implementation of a responsive behavior. It also implements  smooth transitions. Also modern concepts with Box Shadow. Flexbox.
*    **JavaScript:** Creates the necessary application behavior, with functions  like async, await. Also handles all form actions, user selections. Makes calls to  Azure Translation services to the specified server in python , or user's voice to set on the app

 ### Backend

*   **Python:** Uses Flask framework  as its main server and creates routes `/` and `/languages` and the main logic to call Azure APIs (for translations and listing supported languages). Uses Flask’s `render_template`, `request` and `jsonify `for serving HTML, sending data with form requests , json calls
*   **Azure Translator API**: Uses microsoft translation services by API to set calls to microsoft Translation service that gives the application translations power. It requires `KEY` , `ENDPOINT` and  `LOCATION` properties set inside `.env`
*   **python-dotenv:** Manages and keeps api configurations using local `.env` configuration (for environment variables) which allows that your information remains safe.
*   **requests**:  for  http requests actions for connecting with Translation Services using POST and GET methods

### Libraries and external tools:

*  **Font Awesome** for `icons` ( speaker and other icon in project). It's loaded using `CDN`.
*   **Speech Synthesis API** to transform the translated text  into audio using browsers built-in API (` speechSynthesis` ,  `SpeechSynthesisUtterance `) with browser's libraries
*    **Speech Recognition API** to capture users voice and use as input in html text-boxes to translate, is supported using `webkitSpeechRecognition`
*    **Jinja2**: Template Engine (default from flask framework)

## Setup
 1. Clone the repository from Github.
 2. Create an `.env` file in the root directory of the project
  ```bash
      KEY=<Your Azure Translator API Key>
      ENDPOINT=<Your Azure Translator API Endpoint>
      LOCATION=<Your Azure Translator API Location>
      Important: Get Azure API Key, Location , Endpoints to be used inside file.
```
3. Install Dependencies: Navigate to the project folder on your terminal, to set proper configuration
```bash 
pip install flask requests python-dotenv
``` 
4. Run the application
```bash
python app.py
```
## Usage
   1) Enter Text: Input the text you want to translate into the provided textarea box.
   2) Select Language: Choose the desired target language from the dropdown selection list (Spanish, French, German, Italian, or Portuguese, or set the   
      new language by sending to azure, using python).
   3) Translate: click the translate button to see the resulting translated text in the layout/container set for it
   4) Speech Input Press "Voice Input" button, speak after is activated, will enable text input and you can use text translations from speech (Chrome- 
      Based browsers with correct implementations needed, might fail in old versions/different settings of same browsers ). Make a try if recognition and 
      proper browser with configurations exist (otherwise errors from js can be found)
