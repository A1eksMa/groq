# GroqAPI


## About
FastAPI wrapper over GroqAPI.

## Deploy

To run api from container, clone this repository to remoute host:
```bash
git clone https://github.com/A1eksMa/groq/
cd groq
```

Put your groq token into `YOUR_SECRET_GROQ_TOKEN` variable in `groq/config.py` (or create `groq/groq/.env` file).  
Build container from `Dockerfile` and run it:
```bash
docker build -t groq .
docker run -d -p 5555:5555 --name groq groq
```
