from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse
import uvicorn
from config import HOST, PORT
from routers import (
    # Alibaba Cloud
    qwen_qwen3_32b,

    # Deepseek/Meta
    deepseek_r1_distill_llama_70b,
    
    # Google
    gemma2_9b_it,

    # Groq
    compound_beta,
    compound_beta_mini,
    compound_beta_oss,

    # Hugging Face
    distil_whisper_large_v3_en, # depricated

    # Meta
    llama_3_1_8b_instant,
    llama_3_3_70b_versatile,
    llama3_70b_8192, # depricated
    llama3_8b_8192, # depricated
    meta_llama_llama_4_maverick_17b_128e_instruct,
    meta_llama_llama_4_scout_17b_16e_instruct,
    meta_llama_llama_guard_4_12b,
    meta_llama_llama_prompt_guard_2_22m,
    meta_llama_llama_prompt_guard_2_86m,

    # Moonshot AI
    moonshotai_kimi_k2_instruct,

    # Open AI
    openai_gpt_oss_20b,
    openai_gpt_oss_120b,
    whisper_large_v3,
    whisper_large_v3_turbo,

    #Play AI
    playai_tts,
    playai_tts_arabic,
)

app = FastAPI()

# Include all the routers
# Alibaba Cloud
app.include_router(qwen_qwen3_32b.router)

# Deepseek/Meta
app.include_router(deepseek_r1_distill_llama_70b.router)

# Google
app.include_router(gemma2_9b_it.router)

# Groq
app.include_router(compound_beta.router)
app.include_router(compound_beta_mini.router)
app.include_router(compound_beta_oss.router)

# Hugging Face
app.include_router(distil_whisper_large_v3_en.router) # depricated

# Meta
app.include_router(llama_3_1_8b_instant.router)
app.include_router(llama_3_3_70b_versatile.router)
app.include_router(llama3_70b_8192.router) # depricated
app.include_router(llama3_8b_8192.router) # depricated
app.include_router(llama_guard_3_8b.router)
app.include_router(meta_llama_llama_4_maverick_17b_128e_instruct.router)
app.include_router(meta_llama_llama_4_scout_17b_16e_instruct.router)
app.include_router(meta_llama_llama_guard_4_12b.router)
app.include_router(meta_llama_llama_prompt_guard_2_22m.router)
app.include_router(meta_llama_llama_prompt_guard_2_86m.router)

# Moonshot AI
app.include_router(moonshotai_kimi_k2_instruct.router)

# Open AI
app.include_router(openai_gpt_oss_20b.router)
app.include_router(openai_gpt_oss_120b.router)
app.include_router(whisper_large_v3.router)
app.include_router(whisper_large_v3_turbo.router)

# Play AI
app.include_router(playai_tts.router)
app.include_router(playai_tts_arabic.router)

@app.post("/")
async def groq_api_dispatcher(request: Request):
    groq = await request.json()
    api_key = list(groq.keys())[0]
    model = groq[api_key].get("MODEL")

    if not model:
        raise HTTPException(status_code=400, detail="MODEL not specified in the request.")

    # A mapping of models to their respective routers
    model_router_map = {
        # Alibaba Cloud
        "qwen-qwen3-32b": qwen_qwen3_32b.router,
        # Deepseek/Meta
        "deepseek-r1-distill-llama-70b": deepseek_r1_distill_llama_70b.router,
        # Google
        "gemma2-9b-it": gemma2_9b_it.router,
        # Groq
        "compound-beta": compound_beta.router,
        "compound-beta-mini": compound_beta_mini.router,
        "compound-beta-oss": compound_beta_oss.router,
        # Hugging Face
        "distil-whisper-large-v3-en": distil_whisper_large_v3_en.router, # depricated
        # Meta
        "llama-3.1-8b-instant": llama_3_1_8b_instant.router,
        "llama-3.3-70b-versatile": llama_3_3_70b_versatile.router,
        "llama3-70b-8192": llama3_70b_8192.router, # depricated
        "llama3-8b-8192": llama3_8b_8192.router, # depricated
        "meta-llama/llama-4-maverick-17b-128e-instruct": meta_llama_llama_4_maverick_17b_128e_instruct.router,
        "meta-llama/llama-4-scout-17b-16e-instruct": meta_llama_llama_4_scout_17b_16e_instruct.router,
        "meta-llama/llama-guard-4-12b": meta_llama_llama_guard_4_12b.router,
        "meta-llama/llama-prompt-guard-2-22m": meta_llama_llama_prompt_guard_2_22m.router,
        "meta-llama/llama-prompt-guard-2-86m": meta_llama_llama_prompt_guard_2_86m.router,
        # Moonshot AI
        "moonshotai/kimi-k2-instruct": moonshotai_kimi_k2_instruct.router,
        # Open AI
        "openai/gpt-oss-20b": openai_gpt_oss_20b.router,
        "openai/gpt-oss-120b": openai_gpt_oss_120b.router,
        "whisper-large-v3": whisper_large_v3.router,
        "whisper-large-v3-turbo": whisper_large_v3_turbo.router,
        # Play AI
        "playai-tts": playai_tts.router,
        "playai-tts-arabic": playai_tts_arabic.router,
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
