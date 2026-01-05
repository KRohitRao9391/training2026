import google.generativeai as genai
from Backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def call_gemini(prompt: str):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[Gemini Error] {str(e)}"
