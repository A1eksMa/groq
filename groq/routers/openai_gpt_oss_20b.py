from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/openai/gpt-oss-20b")
async def openai_gpt_oss_20b(groq: dict):
    return await handle_text_model_request(groq)
