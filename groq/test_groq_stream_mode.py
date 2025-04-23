from groq import AsyncGroq
from config import default_groq
from config import YOUR_SECRET_GROQ_TOKEN
import asyncio

groq = default_groq
groq["STREAM"] = True
groq["MESSAGES"].append({'role' : 'user', 'content' : 'How to write the Hello World! in java? Give me example and explain  me how it works.'})

async def main():
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

    async for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")

asyncio.run(main())
