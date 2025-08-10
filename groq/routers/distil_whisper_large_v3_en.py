from fastapi import APIRouter

router = APIRouter()

@router.post("/distil-whisper-large-v3-en")
async def distil_whisper_large_v3_en():
    return {"message": "This endpoint is under development."}
