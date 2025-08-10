from fastapi import APIRouter
from .common_text_logic import handle_text_model_request

router = APIRouter()

@router.post("/compound-beta")
async def compound_beta(groq: dict):
    return await handle_text_model_request(groq)

