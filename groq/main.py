from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse
import uvicorn
from config import HOST, PORT
from routers import (
    allam_2_7b,
    compound_beta,
    compound_beta_mini,
    deepseek_r1_distill_llama_70b,
    distil_whisper_large_v3_en,
    gemma2_9b_it,
    llama_3_1_8b_instant,
    llama_3_3_70b_versatile,
    llama_guard_3_8b,
    llama3_70b_8192,
    llama3_8b_8192,
    meta_llama_llama_4_maverick_17b_128e_instruct,
    meta_llama_llama_4_scout_17b_16e_instruct,
    mistral_saba_24b,
    playai_tts,
    playai_tts_arabic,
    qwen_qwq_32b,
    whisper_large_v3,
    whisper_large_v3_turbo,
)

app = FastAPI()

# Include all the routers
app.include_router(allam_2_7b.router)
app.include_router(compound_beta.router)
app.include_router(compound_beta_mini.router)
app.include_router(deepseek_r1_distill_llama_70b.router)
app.include_router(distil_whisper_large_v3_en.router)
app.include_router(gemma2_9b_it.router)
app.include_router(llama_3_1_8b_instant.router)
app.include_router(llama_3_3_70b_versatile.router)
app.include_router(llama_guard_3_8b.router)
app.include_router(llama3_70b_8192.router)
app.include_router(llama3_8b_8192.router)
app.include_router(meta_llama_llama_4_maverick_17b_128e_instruct.router)
app.include_router(meta_llama_llama_4_scout_17b_16e_instruct.router)
app.include_router(mistral_saba_24b.router)
app.include_router(playai_tts.router)
app.include_router(playai_tts_arabic.router)
app.include_router(qwen_qwq_32b.router)
app.include_router(whisper_large_v3.router)
app.include_router(whisper_large_v3_turbo.router)

@app.post("/")
async def groq_api_dispatcher(request: Request):
    groq = await request.json()
    api_key = list(groq.keys())[0]
    model = groq[api_key].get("MODEL")

    if not model:
        raise HTTPException(status_code=400, detail="MODEL not specified in the request.")

    # A mapping of models to their respective routers
    model_router_map = {
        "allam-2-7b": allam_2_7b.router,
        "compound-beta": compound_beta.router,
        "compound-beta-mini": compound_beta_mini.router,
        "deepseek-r1-distill-llama-70b": deepseek_r1_distill_llama_70b.router,
        "distil-whisper-large-v3-en": distil_whisper_large_v3_en.router,
        "gemma2-9b-it": gemma2_9b_it.router,
        "llama-3.1-8b-instant": llama_3_1_8b_instant.router,
        "llama-3.3-70b-versatile": llama_3_3_70b_versatile.router,
        "llama-guard-3-8b": llama_guard_3_8b.router,
        "llama3-70b-8192": llama3_70b_8192.router,
        "llama3-8b-8192": llama3_8b_8192.router,
        "meta-llama/llama-4-maverick-17b-128e-instruct": meta_llama_llama_4_maverick_17b_128e_instruct.router,
        "meta-llama/llama-4-scout-17b-16e-instruct": meta_llama_llama_4_scout_17b_16e_instruct.router,
        "mistral-saba-24b": mistral_saba_24b.router,
        "playai-tts": playai_tts.router,
        "playai-tts-arabic": playai_tts_arabic.router,
        "qwen-qwq-32b": qwen_qwq_32b.router,
        "whisper-large-v3": whisper_large_v3.router,
        "whisper-large-v3-turbo": whisper_large_v3_turbo.router,
    }

    router = model_router_map.get(model)
    if not router:
        return JSONResponse(status_code=404, content={"detail": f"Model '{model}' not found."})

    # This is a simplified way to forward the request.
    # In a real-world scenario, you might need a more robust solution.
    for route in router.routes:
        if route.path == f"/{model}":
            return await route.endpoint(groq)

    return JSONResponse(status_code=500, content={"detail": "Internal server error."})


if __name__=="__main__":
    uvicorn.run(app, host=HOST, port=PORT)