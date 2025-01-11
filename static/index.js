document.addEventListener("DOMContentLoaded", () => {
  const languageSelect = document.getElementById("languageSelect");
  const originalText = document.getElementById("originalText");
  const voiceInputButton = document.getElementById("voiceInputButton");
  const errorMessageDiv = document.getElementById("error-message"); // Error Message
  let currentLanguage = 'en';

  // Fetch languages
  const fetchLanguages = async () => {
      try {
          const response = await fetch("/languages");
          if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
          const languages = await response.json();
          for (const langCode in languages) {
              const option = document.createElement("option");
              option.value = langCode;
              option.textContent = languages[langCode].name;
              languageSelect.appendChild(option);
          }
          languageSelect.value = currentLanguage; // Default
          languageSelect.addEventListener('change', (event) => {
              currentLanguage = event.target.value;
          })
      } catch (error) {
          console.error("Failed to fetch languages:", error);
      }
  };
  const handleSpeakButtonClick = () => {
          const speakButton = document.querySelector(".speak-button");
          if(speakButton)
          {
              speakButton.addEventListener('click', () =>{
                  const translatedResult = document.getElementById("translatedResult").textContent;
                  speakText(translatedResult,currentLanguage);
              })
          }

  }

  const handleFormSubmit = async (event) => {
      event.preventDefault();
      try {
          const formData = new FormData(event.target);
          const response = await fetch("/", {method: "POST", body: formData});
          if (!response.ok) {
               const errorData = await response.text(); // Obtain error details
                 showError(errorData);
          } else {
             errorMessageDiv.style.display = 'none';// Hide error if successful
               document.body.innerHTML = await response.text();
                  handleSpeakButtonClick();
           }

      } catch (error) {
          console.error("Error submitting form or refreshing content:", error);
            showError("An unexpected error occurred while submitting the form.");
      }
  };


 const showError = (message) => {
          errorMessageDiv.textContent = message;
         errorMessageDiv.style.display = "block"; // Display the error message
     };

  const speakText = (text, language) => {
      if ('speechSynthesis' in window) {
          const utterance = new SpeechSynthesisUtterance(text);
          utterance.lang = language;
          speechSynthesis.speak(utterance);
      } else {
          console.error("SpeechSynthesis is not available");
      }
  };

  const startVoiceInput = () => {
      if ('webkitSpeechRecognition' in window) {
          const recognition = new webkitSpeechRecognition();
          recognition.continuous = false;
          recognition.lang = currentLanguage;
          recognition.onstart = function () {
              voiceInputButton.disabled = true;
              originalText.placeholder = 'Listening...';
          };
          recognition.onresult = (event) => {
              const transcript = event.results[0][0].transcript;
              originalText.value = transcript;
              originalText.placeholder = "Enter text to translate";
              voiceInputButton.disabled = false;
              recognition.stop();
          };
           recognition.onerror = (event) => {
               console.error("Error occurred with the speech recognitions:", event.error) // feedback dev or code action/issue if needed.
                voiceInputButton.disabled = false; // enable action again
                recognition.stop();  // ensure everything goes smooth , prevent actions not stop when a recording error occurred (for future use case or problems, if recognition crashed for network reason the app would enable record again)
                originalText.placeholder = "Enter text to translate"

           };
           recognition.start();
      } else {
          console.error("Your browser doesn't support  speech  recognition.");
      }
  };
  fetchLanguages();
  handleSpeakButtonClick() //Ensure speaker click is on
  document.getElementById('translation-form').addEventListener('submit', handleFormSubmit);
  voiceInputButton.addEventListener('click', startVoiceInput);
});