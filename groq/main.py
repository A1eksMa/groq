from groq import AsyncGroq
from fastapi import FastAPI, Response
import uvicorn
from config import HOST, PORT
from config import default_groq
from config import YOUR_SECRET_GROQ_TOKEN
import asyncio

app = FastAPI()

async def handle_groq(groq):
    client = AsyncGroq(api_key=groq["YOUR_SECRET_GROQ_TOKEN"])
    if groq["STREAM"]:
        async for message in client.chat.completions.create(
                model=groq["MODEL"],
                messages=groq["MESSAGES"],
                temperature=groq["TEMPERATURE"],
                max_completion_tokens=groq["MAX_COMPLETION_TOKENS"],
                top_p=groq["TOP_P"],
                stream=groq["STREAM"],
                stop=groq["STOP"],
            ):
            yield message.choices[0].message.content
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
        yield completion.choices[0].message.content

async def stream_response(groq):
    gen = handle_groq(groq)
    while True:
        try:
            chunk = await gen.__anext__()
            if chunk == "":
                break
            yield chunk
        except StopAsyncIteration:
            break

@app.post("/")
async def groq_api(groq: dict = default_groq):
    if groq["STREAM"]:
        async def stream():
            async for chunk in stream_response(groq):
                yield chunk + "\\n"
        return Response(stream(), media_type="text/event-stream")
    else:
        gen = handle_groq(groq)
        return {"result": await gen.__anext__()}

@app.get("/groq_single_prompt")
async def groq_single_prompt(prompt: str):
    if True:
        global YOUR_SECRET_GROQ_TOKEN
        groq = {"YOUR_SECRET_GROQ_TOKEN" : YOUR_SECRET_GROQ_TOKEN,
            "MODEL" : "llama-3.3-70b-versatile",
            "MESSAGES" : [{'role' : 'user', 'content' : prompt}],
            "TEMPERATURE" : 1,
	    "MAX_COMPLETION_TOKENS": 1024,
	    "TOP_P": 1,
            "STREAM": False,
            "STOP": None,
           }
        client = AsyncGroq(api_key=groq["YOUR_SECRET_GROQ_TOKEN"])
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
    else:
        return "The service is temporarily unavailable."
	    
if __name__=="__main__":
    uvicorn.run(app, host=HOST, port=PORT)
