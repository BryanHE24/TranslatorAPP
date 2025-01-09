document.addEventListener("DOMContentLoaded", function () {
    console.log("Page loaded");

    // Ensure that elements are properly styled and made visible after the DOM is fully loaded
    document.querySelector('.container').style.display = 'block'; // Ensure container is visible

    // Debugging logs
    console.log("Container should be visible now");

    // Ensure select and textarea are visible on load
    document.querySelector('select').style.visibility = 'visible';
    document.querySelector('textarea').style.visibility = 'visible';

    // Debug logs
    console.log("Select and Textarea visibility set");

    // Ensure that dark mode settings are checked and applied
    if (localStorage.getItem('dark-mode') === 'enabled') {
        document.body.classList.add('dark-mode');
        document.querySelector('.container').classList.add('dark-mode');
        document.getElementById('dark-mode-toggle').classList.add('dark-mode');
    }

    // Dark Mode Toggle
    document.getElementById('dark-mode-toggle').addEventListener('click', () => {
        // Toggle dark mode on body and container
        document.body.classList.toggle('dark-mode');
        document.querySelector('.container').classList.toggle('dark-mode');
        document.getElementById('dark-mode-toggle').classList.toggle('dark-mode');

        // Save dark mode state
        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('dark-mode', 'enabled');
        } else {
            localStorage.setItem('dark-mode', 'disabled');
        }
    });

    // Handle voice input for translation
    const voiceButton = document.getElementById('voice-input');
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

    recognition.onresult = function (event) {
        const transcript = event.results[0][0].transcript;
        document.querySelector('textarea[name="text"]').value = transcript;
    };

    voiceButton.addEventListener('click', () => {
        recognition.start();
    });

    // Debugging end of script load
    console.log("JS script fully loaded and initialized");
});
