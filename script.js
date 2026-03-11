function analyzeSentiment() {
    const review = document.getElementById('reviewInput').value.toLowerCase();
    const resultDisplay = document.getElementById('resultDisplay');

  
    const positiveWords = ['amazing', 'good', 'great', 'fantastic', 'love'];
    const negativeWords = ['boring', 'bad', 'worst', 'terrible', 'hate'];

    let score = 0;
    if (positiveWords.some(word => review.includes(word))) score++;
    if (negativeWords.some(word => review.includes(word))) score--;

    if (score > 0) {
        resultDisplay.innerText = "Result: Positive 😊";
    } else if (score < 0) {
        resultDisplay.innerText = "Result: Negative 😞";
    } else {
        resultDisplay.innerText = "Result: Neutral 😐";
    }
}
