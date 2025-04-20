from groq import Groq
from fastapi import FastAPI
import uvicorn
from config import HOST, PORT
from config import default_groq
from config import YOUR_SECRET_GROQ_TOKEN

app = FastAPI()

@app.post("/")
def groq_api(groq: dict = default_groq):
    """
    Example of usage.
    Set `groq` variable:
    groq = {"YOUR_SECRET_GROQ_TOKEN" : YOUR_SECRET_GROQ_TOKEN,
            "MODEL" : "llama-3.3-70b-versatile",
            "MESSAGES" : list(),
            "TEMPERATURE" : 1,
	    "MAX_COMPLETION_TOKENS": 1024,
	    "TOP_P": 1,
            "STREAM": False,
            "STOP": None,
           }
    """
    if groq["STREAM"]:
        pass
    else:
        client = Groq(api_key=groq["YOUR_SECRET_GROQ_TOKEN"])
        completion = client.chat.completions.create(
            model=groq["MODEL"],
            messages=groq["MESSAGES"],
            temperature=groq["TEMPERATURE"],
            max_completion_tokens=groq["MAX_COMPLETION_TOKENS"],
            top_p=groq["TOP_P"],
            stream=groq["STREAM"],
            stop=groq["STOP"],
        )
        return completion.choices[0].message.content

@app.get("/groq_single_prompt")
def groq_single_prompt(prompt: str):
    if True:
        global YOUR_SECRET_GROQ_TOKEN
        groq = {"YOUR_SECRET_GROQ_TOKEN" : YOUR_SECRET_GROQ_TOKEN,
            "MODEL" : "llama-3.3-70b-versatile",
            "MESSAGES" : list({'role' : 'user', 'content' : prompt}),
            "TEMPERATURE" : 1,
	    "MAX_COMPLETION_TOKENS": 1024,
	    "TOP_P": 1,
            "STREAM": False,
            "STOP": None,
           }
        client = Groq(api_key=groq["YOUR_SECRET_GROQ_TOKEN"])
        completion = client.chat.completions.create(
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
