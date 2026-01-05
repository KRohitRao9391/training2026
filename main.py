import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Backend.models import PromptRequest
from Backend.Servers.openai_service import call_openai
from Backend.Servers.claude_service import call_claude
from Backend.Servers.gemini_service import call_gemini

app = FastAPI(title="LLM Comparison API:")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/compare")
async def compare_lims(data: PromptRequest):
    prompt = data.prompt
    openai_res, gemini_res, claude_res = await asyncio.gather(
        call_openai(prompt),
        call_gemini(prompt),
        call_claude(prompt)
    )

    return {
        "OpenAI": openai_res,
        "Claude": claude_res,
        "Gemini": gemini_res
    }
