import requests

# Set GroqAPI parametres
GROQ_TOKEN = "YOUR_SECRET_GROQ_TOKEN"
MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0
MESSAGES = list()


groq = {"GROQ_TOKEN" : GROQ_TOKEN,
        "MODEL" : MODEL,
        "TEMPERATURE" : TEMPERATURE,
        "MESSAGES" : MESSAGES}


if __name__=="__main__":
    # Example of usage the `groq_api`
    url = "http://localhost:5555/groq_api/"
    groq["MESSAGES"].append({'role' : 'user', 'content' : "Tell me 'Hello!'"})
    response = requests.post(url,json=groq).text
    print(response)
    groq["MESSAGES"] = list()

    # Example of usage the `groq_single_prompt`
    url = "http://localhost:5555/groq_single_prompt/"
    response = requests.get(url,params={"prompt" : "Tell me 'Hello!'"}).text
    print(response)

    # Example of usage the `groq_chat`
    url = "http://localhost:5555/groq_chat/"
    response = requests.get(url,params={"prompt" : "Tell me any number."}).text
    print(response)
    response = requests.get(url,params={"prompt" : "Repeat me the number, that you said."}).text
    print(response)
