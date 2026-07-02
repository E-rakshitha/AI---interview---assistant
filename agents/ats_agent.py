from llm.gemini import GeminiClient

client = GeminiClient()


def ats_score(resume_text):

    prompt = f"""
You are an expert ATS (Applicant Tracking System).

Analyze the following resume.

Resume:
{resume_text}

Provide the response ONLY in the following format.

ATS Score: x/100

Skills Match:
x%

Missing Keywords:
- Keyword 1
- Keyword 2
- Keyword 3
- Keyword 4

Strengths:
- Point 1
- Point 2
- Point 3

Weaknesses:
- Point 1
- Point 2
- Point 3

Suggestions:
- Point 1
- Point 2
- Point 3
"""

    return client.generate(prompt)