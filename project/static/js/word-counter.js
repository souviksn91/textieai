// static/js/word-counter.js
document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text-input');
    const wordCounter = document.getElementById('word-counter');

    if (textInput && wordCounter) {
        textInput.addEventListener('input', updateWordCounter);

        function updateWordCounter() {
            const text = textInput.value.trim();
            const wordCount = text ? text.split(/\s+/).length : 0;
            wordCounter.textContent = `${wordCount}/30 words`;
            wordCounter.style.color = wordCount > 30 ? 'red' : '#666';
        }

        // Initialize counter on page load
        updateWordCounter();
    }
});