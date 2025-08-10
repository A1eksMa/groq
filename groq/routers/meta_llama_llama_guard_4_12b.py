from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/meta-llama/llama-guard-4-12b")
async def meta_llama_llama_guard_4_12b(groq: dict):
    return await handle_text_model_request(groq)
