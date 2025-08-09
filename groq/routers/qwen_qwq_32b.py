from fastapi import APIRouter

router = APIRouter()

@router.post("/qwen-qwq-32b")
async def qwen_qwq_32b():
    return {"message": "This endpoint is under development."}
