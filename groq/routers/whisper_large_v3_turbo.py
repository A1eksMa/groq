from fastapi import APIRouter

router = APIRouter()

@router.post("/whisper-large-v3-turbo")
async def whisper_large_v3_turbo():
    return {"message": "This endpoint is under development."}
