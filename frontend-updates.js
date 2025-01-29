// Remplacer la fonction getGeminiSuggestions par :
async function getGeminiSuggestions(content, type) {
    try {
        const endpoint = type === 'CV' ? '/api/analyze-cv' : '/api/analyze-offer';
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(
                type === 'CV' ? {
                    name: document.getElementById('name').value,
                    education: document.getElementById('education').value,
                    experience: document.getElementById('experience').value,
                    skills: document.getElementById('skills').value
                } : {
                    company: document.getElementById('company').value,
                    position: document.getElementById('position').value,
                    description: document.getElementById('description').value,
                    requirements: document.getElementById('requirements').value
                }
            )
        });
        
        const data = await response.json();
        return data.analysis;
    } catch (error) {
        console.error('Error getting analysis:', error);
        return 'Unable to get AI suggestions at this time.';
    }
}
