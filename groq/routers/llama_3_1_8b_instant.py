from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/llama-3.1-8b-instant")
async def llama_3_1_8b_instant(groq: dict):
    return await handle_text_model_request(groq)

