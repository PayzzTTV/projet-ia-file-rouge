from flask import Flask, request, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)

GEMINI_API_KEY = 'AIzaSyBmHFOoDSMU-S9X8NGizErNI6ZC4A-G9b0'
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'

class GeminiPrompts:
    @staticmethod
    def get_cv_analysis_prompt(cv_data):
        return f"""
        Analyze the following CV for an apprenticeship position and provide detailed feedback:

        Background:
        - Name: {cv_data.get('name')}
        - Education: {cv_data.get('education')}
        - Experience: {cv_data.get('experience')}
        - Skills: {cv_data.get('skills')}

        Please provide feedback on:
        1. CV Structure and Clarity
        2. Relevance of experience for apprenticeship positions
        3. Skills assessment
        4. Suggested improvements
        5. Potential types of apprenticeships that would be a good fit

        Format the response in clear sections with specific, actionable recommendations.
        """

    @staticmethod
    def get_job_offer_analysis_prompt(offer_data):
        return f"""
        Analyze the following apprenticeship job offer and provide detailed feedback:

        Company: {offer_data.get('company')}
        Position: {offer_data.get('position')}
        Description: {offer_data.get('description')}
        Requirements: {offer_data.get('requirements')}

        Please analyze and provide feedback on:
        1. Clarity and completeness of the job description
        2. Appropriateness of requirements for an apprenticeship position
        3. Suggested improvements to attract better candidates
        4. Additional skills or requirements that should be mentioned
        5. Potential red flags or missing important information

        Ensure the feedback is constructive and specific to apprenticeship positions.
        """

def call_gemini_api(prompt):
    try:
        headers = {
            'Content-Type': 'application/json',
        }
        
        payload = {
            'contents': [{
                'parts': [{
                    'text': prompt
                }]
            }]
        }
        
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=payload
        )
        
        response.raise_for_status()
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"

@app.route('/api/analyze-cv', methods=['POST'])
def analyze_cv():
    cv_data = request.json
    prompt = GeminiPrompts.get_cv_analysis_prompt(cv_data)
    analysis = call_gemini_api(prompt)
    
    return jsonify({
        'analysis': analysis,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/analyze-offer', methods=['POST'])
def analyze_offer():
    offer_data = request.json
    prompt = GeminiPrompts.get_job_offer_analysis_prompt(offer_data)
    analysis = call_gemini_api(prompt)
    
    return jsonify({
        'analysis': analysis,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True)