from groq import Groq
from fastapi import FastAPI
import uvicorn
from config import HOST, PORT
from config import GROQ_TOKEN, MODEL, TEMPERATURE, MESSAGES
from config import groq

app = FastAPI()
messages = list()

def response(groq: dict):
    answer = Groq(api_key=groq["GROQ_TOKEN"])\
	         .chat\
	         .completions\
	         .create(model=groq["MODEL"],
	                 messages=groq["MESSAGES"],
     		         temperature=groq["TEMPERATURE"])\
             .choices[0]\
	         .message\
	         .content
    return answer

@app.post("/groq_api")
def groq_api(groq: dict):
    return response(groq)
    
@app.get("/groq_single_prompt")
def groq_single_prompt(prompt: str, groq=groq):
    groq["MESSAGES"].append({'role' : 'user', 'content' : prompt})
    answer = response(groq)
    groq["MESSAGES"] = list()
    return answer

@app.get("/groq_chat")
def groq_chat_10_messages(prompt: str, groq=groq):
    global messages
    messages.append({'role' : 'user', 'content' : prompt})
    groq["MESSAGES"] = messages
    answer = response(groq)
    messages.append({'role' : 'assistant', 'content' : answer})
    groq["MESSAGES"] = list()
    if len(messages) > 10: messages = messages[-10:]
    return answer

if __name__=="__main__":
    uvicorn.run(app, host=HOST, port=PORT)
