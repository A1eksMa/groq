from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/llama3-8b-8192")
async def llama3_8b_8192(groq: dict):
    return await handle_text_model_request(groq)

