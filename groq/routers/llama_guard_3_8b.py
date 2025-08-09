from fastapi import APIRouter

router = APIRouter()

@router.post("/llama-guard-3-8b")
async def llama_guard_3_8b():
    return {"message": "This endpoint is under development."}
