# GroqAPI

FastAPI wrapper over GroqAPI.
Set a few endpoints, that configures AI chat.

`config.py`

Contains default settings: host IP adress, port

`server.py`

FastAPI server with three endpoints:
- **groq_api**: for advanced usage, allow set custom settings and preferences of GroqAPI
- **groq_single_prompt**: one prompt - one response, default settings
- **groq_chat**: get the prompt, save context (last 10 messages)

`client.py`

Examples of usage
