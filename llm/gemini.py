import os
import google.generativeai as genai
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

print("Loaded API Key:", API_KEY[:10] + "...")
print("Model:", MODEL_NAME)

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=API_KEY)


class GeminiClient:

    def __init__(self):
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate(self, prompt: str):
        try:
            response = self.model.generate_content(prompt)
            return response.text

        except ResourceExhausted:
            return "ERROR: Gemini API quota exceeded."

        except Exception as e:
            return f"ERROR: {e}"