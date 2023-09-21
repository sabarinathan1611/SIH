// Tokenize a text into words
function tokenize(text) {
    return text.toLowerCase().split(/\W+/).filter(word => word.length > 0);
}

// Calculate cosine similarity between two tokenized texts
function cosineSimilarity(text1, text2) {
    const tokens1 = tokenize(text1);
    const tokens2 = tokenize(text2);

    // Calculate the dot product of the token vectors
    let dotProduct = 0;
    for (const token of tokens1) {
        if (tokens2.includes(token)) {
            dotProduct++;
        }
    }

    // Calculate the magnitude (Euclidean norm) of the token vectors
    const magnitude1 = Math.sqrt(tokens1.length);
    const magnitude2 = Math.sqrt(tokens2.length);

    // Calculate the cosine similarity
    const similarity = dotProduct / (magnitude1 * magnitude2);

    return similarity;
}

// Handle the button click event
document.getElementById("calculateButton").addEventListener("click", function() {
    const text1 = document.getElementById("text1").value;
    const text2 = document.getElementById("text2").value;

    const similarity = cosineSimilarity(text1, text2);
    document.getElementById("result").innerHTML = `Cosine Similarity: ${similarity}`;
});
