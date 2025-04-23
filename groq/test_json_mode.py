from groq import AsyncGroq
from config import default_groq
from config import YOUR_SECRET_GROQ_TOKEN
import asyncio

groq = default_groq
groq["MESSAGES"].append({'role' : 'system', 'content' : 'Always return me json, that looks like a:{"ANSWER": text string with your message}'})
groq["MESSAGES"].append({'role' : 'user', 'content' : 'Hello'})

async def main():
    client = AsyncGroq(api_key=groq["YOUR_SECRET_GROQ_TOKEN"])
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
    print(completion.choices[0].message.content)

asyncio.run(main())
