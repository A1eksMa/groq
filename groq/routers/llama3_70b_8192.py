from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/llama3-70b-8192")
async def llama3_70b_8192(groq: dict):
    return await handle_text_model_request(groq)

