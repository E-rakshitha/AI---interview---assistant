from llm.gemini import GeminiClient
import json

client = GeminiClient()


def analyze_resume(resume_text):

    prompt = f"""
You are an expert Resume Analyzer.

Analyze the resume.

Return ONLY valid JSON.

Do NOT use markdown.
Do NOT use ```json.
Do NOT explain anything.

Format:

{{
    "candidate_name": "",
    "education": "",
    "skills": [],
    "projects": [],
    "experience": "",
    "strengths": []
}}

Resume:

{resume_text}
"""

    response = client.generate(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        return json.loads(response)

    except Exception:

        return {
            "candidate_name": "",
            "education": "",
            "skills": [],
            "projects": [],
            "experience": "",
            "strengths": [],
            "raw_response": response
        }