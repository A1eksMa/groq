from groq import AsyncGroq
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn
from config import HOST, PORT
from config import default_groq
from config import YOUR_SECRET_GROQ_TOKEN
import asyncio

app = FastAPI()

async def stream(completion):
    async for chunk in completion:
        yield chunk.choices[0].delta.content or ""

@app.post("/")
async def groq_api(groq: dict):
	
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
	    
if __name__=="__main__":
    uvicorn.run(app, host=HOST, port=PORT)
