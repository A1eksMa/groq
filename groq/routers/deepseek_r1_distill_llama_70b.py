from fastapi import APIRouter

router = APIRouter()

@router.post("/deepseek-r1-distill-llama-70b")
async def deepseek_r1_distill_llama_70b():
    return {"message": "This endpoint is under development."}
