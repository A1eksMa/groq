from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/meta-llama/llama-4-scout-17b-16e-instruct")
async def meta_llama_llama_4_scout_17b_16e_instruct(groq: dict):
    return await handle_text_model_request(groq)

