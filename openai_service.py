import openai
from Backend.config import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

async def call_openai(prompt: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
