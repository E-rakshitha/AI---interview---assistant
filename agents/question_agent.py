from llm.gemini import GeminiClient

client = GeminiClient()


def generate_questions(resume_text):

    prompt = f"""
You are an experienced Technical Interviewer.

Based on the following resume, generate exactly 10 interview questions.

Rules:
- Return ONLY the questions.
- Number them from 1 to 10.
- No explanations.
- No introduction.

Resume:
{resume_text}
"""

    return client.generate(prompt)