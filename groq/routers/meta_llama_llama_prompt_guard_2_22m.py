from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/meta-llama/llama-prompt-guard-2-22m")
async def meta_llama_llama_prompt_guard_2_22m(groq: dict):
    return await handle_text_model_request(groq)
