const sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    // Add more sentences here
];

const sentenceElement = document.getElementById('sentence');
const userInput = document.getElementById('userInput');
const startButton = document.getElementById('startButton');
const result = document.getElementById('result');
const wpmElement = document.getElementById('wpm');
const nextButton = document.getElementById('nextButton');

let currentSentenceIndex = 0;
let startTime, endTime;

function calculateWPM() {
    const totalTime = (endTime - startTime) / 1000; // in seconds
    const wordsPerMinute = (sentenceElement.innerText.split(' ').length / totalTime) * 60;
    wpmElement.innerText = wordsPerMinute.toFixed(2);
}

function loadNextSentence() {
    if (currentSentenceIndex < sentences.length - 1) {
        currentSentenceIndex++;
        sentenceElement.innerText = sentences[currentSentenceIndex];
        userInput.value = '';
        result.innerText = '';
        wpmElement.innerText = '0.00';
        userInput.focus();
    } else {
        // Handle the case where all sentences have been completed
        sentenceElement.innerText = "You've completed all sentences!";
        userInput.value = '';
        result.innerText = '';
        wpmElement.innerText = '0.00';
        nextButton.disabled = true;
    }
}

startButton.addEventListener('click', function () {
    userInput.focus();
    sentenceElement.classList.add('active');
    startButton.style.display = 'none';
    userInput.value = '';
    startTime = Date.now();
});

userInput.addEventListener('input', function () {
    if (userInput.value === sentenceElement.innerText) {
        endTime = Date.now();
        calculateWPM();
    }
});

userInput.addEventListener('keyup', function (event) {
    if (event.key === 'Enter' && userInput.value === sentenceElement.innerText) {
        endTime = Date.now();
        calculateWPM();
    }
});

nextButton.addEventListener('click', function () {
    loadNextSentence();
});

loadNextSentence();
