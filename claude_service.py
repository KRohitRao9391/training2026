import anthropic
from Backend.config import CLAUDE_API_KEY

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def call_claude(prompt: str):
    response = client.message.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            temperature=0.7,
        
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    return response.content[0].text
