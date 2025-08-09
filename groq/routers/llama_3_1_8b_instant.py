from fastapi import APIRouter

router = APIRouter()

@router.post("/llama-3.1-8b-instant")
async def llama_3_1_8b_instant():
    return {"message": "This endpoint is under development."}
