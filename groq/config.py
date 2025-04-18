from dotenv import dotenv_values
config = dotenv_values()

HOST="0.0.0.0"
PORT=5555

YOUR_SECRET_GROQ_TOKEN = config.get("GROQ_TOKEN")

default_groq = {"YOUR_SECRET_GROQ_TOKEN" : YOUR_SECRET_GROQ_TOKEN,
            "MODEL" : "llama-3.3-70b-versatile",
            "MESSAGES" : list(),
            "TEMPERATURE" : 1,
	    "MAX_COMPLETION_TOKENS": 1024,
	    "TOP_P": 1,
            "STREAM": False,
            "STOP": None,
           }
