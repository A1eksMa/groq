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
	
    client = AsyncGroq(api_key=groq["YOUR_SECRET_GROQ_TOKEN"])
	
    if groq["STREAM"]:
        completion = await client.chat.completions.create(
            model=groq["MODEL"],
            messages=groq["MESSAGES"],
            temperature=groq["TEMPERATURE"],
            max_completion_tokens=groq["MAX_COMPLETION_TOKENS"],
            top_p=groq["TOP_P"],
            stream=groq["STREAM"],
            stop=groq["STOP"],
            )
        return StreamingResponse(stream(completion), media_type="text/plain")
    else:
        if "RESPONSE_FORMAT" in groq.keys():
            completion = await client.chat.completions.create(
                model=groq["MODEL"],
                messages=groq["MESSAGES"],
                temperature=groq["TEMPERATURE"],
                max_completion_tokens=groq["MAX_COMPLETION_TOKENS"],
                top_p=groq["TOP_P"],
                stream=groq["STREAM"],
                response_format={'type': 'json_object'},
                stop=groq["STOP"],
                )
        else:
            completion = await client.chat.completions.create(
                model=groq["MODEL"],
                messages=groq["MESSAGES"],
                temperature=groq["TEMPERATURE"],
                max_completion_tokens=groq["MAX_COMPLETION_TOKENS"],
                top_p=groq["TOP_P"],
                stream=groq["STREAM"],
                stop=groq["STOP"],
                )
        return completion.choices[0].message.content
	    
if __name__=="__main__":
    uvicorn.run(app, host=HOST, port=PORT)
