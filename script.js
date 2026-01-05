async function Compare() {
    const prompt = document.getElementById('prompt').value;

    // Clear previous results
    document.getElementById('openai').textContent = '';
    document.getElementById('claude').textContent = '';
    document.getElementById('gemini').textContent = '';

    try {
        const response = await fetch('http://localhost:8000/compare', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: prompt }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        document.getElementById('openai').textContent = data.OpenAI;
        document.getElementById('claude').textContent = data.Claude;
        document.getElementById('gemini').textContent = data.Gemini;
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while comparing models. Please check the console for details.');
    }
}
