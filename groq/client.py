import requests

from config import HOST, PORT
from config import GROQ_TOKEN, MODEL, TEMPERATURE, MESSAGES
from config import groq


if __name__=="__main__":
    # Example of usage the `groq_api`
    url = f"http://{HOST}:{PORT}/groq_api/"
    groq["MESSAGES"].append({'role' : 'user', 'content' : "Tell me 'Hello!'"})
    response = requests.post(url,json=groq).text
    print(response)
    groq["MESSAGES"] = list()

    # Example of usage the `groq_single_prompt`
    url = f"http://{HOST}:{PORT}/groq_single_prompt/"
    response = requests.get(url,params={"prompt" : "Tell me 'Hello!'"}).text
    print(response)

    # Example of usage the `groq_chat`
    url = f"http://{HOST}:{PORT}/groq_chat/"
    response = requests.get(url,params={"prompt" : "Tell me any number."}).text
    print(response)
    response = requests.get(url,params={"prompt" : "Repeat me the number, that you said."}).text
    print(response)
