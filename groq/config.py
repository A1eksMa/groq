from dotenv import dotenv_values
config = dotenv_values()

HOST="0.0.0.0"
PORT=5555

GROQ_TOKEN = config.get("GROQ_TOKEN")
MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0
MESSAGES = list()

groq = {"GROQ_TOKEN" : GROQ_TOKEN,
        "MODEL" : MODEL,
        "TEMPERATURE" : TEMPERATURE,
        "MESSAGES" : MESSAGES}
