from fastapi import APIRouter
from groq import AsyncGroq
from fastapi.responses import StreamingResponse
import asyncio

router = APIRouter()

async def stream(completion):
    async for chunk in completion:
        yield chunk.choices[0].delta.content or ""

@router.post("/llama-3.3-70b-versatile")
async def llama_3_3_70b_versatile(groq: dict):
    api_key = list(groq.keys())[0]
    params = groq[api_key]
    client = AsyncGroq(api_key=api_key)

    if params["STREAM"]:
        completion = await client.chat.completions.create(
            model=params["MODEL"],
            messages=params["MESSAGES"],
            temperature=params["TEMPERATURE"],
            max_completion_tokens=params["MAX_COMPLETION_TOKENS"],
            top_p=params["TOP_P"],
            stream=params["STREAM"],
            stop=params["STOP"],
        )
        return StreamingResponse(stream(completion), media_type="text/plain")
    else:
        if "RESPONSE_FORMAT" in params.keys():
            completion = await client.chat.completions.create(
                model=params["MODEL"],
                messages=params["MESSAGES"],
                temperature=params["TEMPERATURE"],
                max_completion_tokens=params["MAX_COMPLETION_TOKENS"],
                top_p=params["TOP_P"],
                stream=params["STREAM"],
                response_format={'type': 'json_object'},
                stop=params["STOP"],
            )
        else:
            completion = await client.chat.completions.create(
                model=params["MODEL"],
                messages=params["MESSAGES"],
                temperature=params["TEMPERATURE"],
                max_completion_tokens=params["MAX_COMPLETION_TOKENS"],
                top_p=params["TOP_P"],
                stream=params["STREAM"],
                stop=params["STOP"],
            )
        return completion.choices[0].message.content
