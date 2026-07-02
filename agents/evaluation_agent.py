from llm.gemini import GeminiClient

client = GeminiClient()


def evaluate_answer(questions, answers):

    prompt = f"""
You are an experienced Technical Interviewer.

Evaluate the candidate based on the interview questions and answers.

Questions:
{questions}

Answers:
{answers}

Give the response ONLY in the following format.

Overall Score: x/10
Technical Knowledge: x/10
Communication Skills: x/10
Problem Solving: x/10
Confidence Level: x/10

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

Hiring Recommendation:
Selected
OR
Maybe Selected
OR
Not Selected
"""

    return client.generate(prompt)