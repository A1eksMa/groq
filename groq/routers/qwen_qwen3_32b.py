from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/qwen/qwen3-32b")
async def qwen_qwen3_32b(groq: dict):
    return await handle_text_model_request(groq)
