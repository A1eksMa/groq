from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/meta-llama/llama-4-maverick-17b-128e-instruct")
async def meta_llama_llama_4_maverick_17b_128e_instruct(groq: dict):
    return await handle_text_model_request(groq)

