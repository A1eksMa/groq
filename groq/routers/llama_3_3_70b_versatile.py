from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/llama-3.3-70b-versatile")
async def llama_3_3_70b_versatile(groq: dict):
    return await handle_text_model_request(groq)

