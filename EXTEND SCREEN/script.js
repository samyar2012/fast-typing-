const sentence = document.getElementById('sentence');
const userInput = document.getElementById('userInput');
const startButton = document.getElementById('startButton');
const result = document.getElementById('result');

let startTime, endTime;

startButton.addEventListener('click', function () {
    userInput.focus();
    sentence.classList.add('active');
    startTime = Date.now();
    startButton.style.display = 'none';
});

userInput.addEventListener('input', function () {
    if (userInput.value === sentence.innerText) {
        endTime = Date.now();
        const totalTime = (endTime - startTime) / 1000; // in seconds
        const wordsPerMinute = (sentence.innerText.split(' ').length / totalTime) * 60;
        result.innerText = `Your typing speed: ${wordsPerMinute.toFixed(2)} WPM`;
    }
});
