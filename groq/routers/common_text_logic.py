from groq import AsyncGroq
from fastapi.responses import StreamingResponse

async def stream(completion):
    async for chunk in completion:
        yield chunk.choices[0].delta.content or ""

async def handle_text_model_request(groq: dict):
    api_key = list(groq.keys())[0]
    params = groq[api_key]
    client = AsyncGroq(api_key=api_key)

    if params.get("STREAM", False):
        completion = await client.chat.completions.create(
            model=params["MODEL"],
            messages=params["MESSAGES"],
            temperature=params.get("TEMPERATURE"),
            max_tokens=params.get("MAX_COMPLETION_TOKENS"),
            top_p=params.get("TOP_P"),
            stream=True,
            stop=params.get("STOP"),
        )
        return StreamingResponse(stream(completion), media_type="text/plain")
    else:
        completion_params = {
            "model": params["MODEL"],
            "messages": params["MESSAGES"],
            "temperature": params.get("TEMPERATURE"),
            "max_tokens": params.get("MAX_COMPLETION_TOKENS"),
            "top_p": params.get("TOP_P"),
            "stream": False,
            "stop": params.get("STOP"),
        }
        if "RESPONSE_FORMAT" in params:
            completion_params["response_format"] = params["RESPONSE_FORMAT"]
        
        completion = await client.chat.completions.create(**completion_params)
        return completion.choices[0].message.content
