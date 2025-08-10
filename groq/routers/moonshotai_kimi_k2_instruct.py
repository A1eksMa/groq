from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/moonshotai/kimi-k2-instruct")
async def moonshotai_kimi_k2_instruct(groq: dict):
    return await handle_text_model_request(groq)
