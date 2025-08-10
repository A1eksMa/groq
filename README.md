# GroqAPI



## About
FastAPI wrapper over GroqAPI. 

## Deploy

To run the API from container, clone this repository to remoute host:
```bash
git clone https://github.com/A1eksMa/groq/
```

Put your groq token into `YOUR_SECRET_GROQ_TOKEN` variable in the `groq/groq/config.py` (or create `groq/groq/.env` file).  
To configure port in the `PORT` variable in the `groq/config.py`.  
Build the container from `Dockerfile` and run it:
```bash
docker build -t groq .
docker run -d -p 5555:5555 --name groq groq
```

## Usage

To use API you need the Groq API token from [console.groq.com](https://console.groq.com).  

The main endpoint of the API transfer to original Groq API 8 params.  
Build the dictionary with a Groq API parametres and send a POST request to API.

## Endpoints

The API has a main dispatcher endpoint `/` that routes requests to model-specific endpoints based on the `MODEL` parameter in the request body.

### `/` (Dispatcher)

This is the main entry point. It expects a POST request with a JSON body similar to the `groq_api_params` structure described below. It inspects the `MODEL` field and forwards the request to the appropriate model-specific endpoint. If the model is not found, it returns a 404 error.

### Model-Specific Endpoints

#### Text Mode Models
This endpoints is fully functional and provides the core logic for interacting with the Groq API. It supports normal, JSON, and streaming modes as shown in the examples below.
- `/qwen-qwen3-32b`
- `/deepseek-r1-distill-llama-70b`
- `/gemma2-9b-it`
- and others.


#### Multimodal Models (text-to-speech and `whisper` family)
The following model endpoints are currently implemented as placeholders. They will return a simple JSON response indicating that they are under development.
- `/distil-whisper-large-v3-en`
- `/whisper-large-v3`
- `/whisper-large-v3-turbo`
- `/playai-tts`
- `/playai-tts-arabic`


## Examples
The following examples show how to use the main dispatcher endpoint `/`. The dispatcher will automatically route the request to the correct model endpoint based on the `"MODEL"` field.

```
groq_api_params = {
    "YOUR_SECRET_GROQ_TOKEN": {
        "MODEL": model: str,
        "MESSAGES": messages: Iterable[ChatCompletionMessageParam],
        "TEMPERATURE": temperature: Optional[float] | NotGiven = NOT_GIVEN,
        "MAX_COMPLETION_TOKENS": max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        "TOP_P": top_p: Optional[float] | NotGiven = NOT_GIVEN,
        "STREAM": stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        "RESPONSE_FORMAT": response_format: Optional[completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        "STOP": stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
    }
}
```
(see [Groq API](https://github.com/groq/groq-python/) for details)  

A `messages` contains the context, and looks like a list of dict:
```
[
    {
        'role' : 'user',
        'content' : prompt,
    },
    {
        'role' : 'assistant',
        'content' : response,
    },
]
```

Select a `model` from the list of available models:
- "qwen-qwen3-32b",
- "deepseek-r1-distill-llama-70b",
- "gemma2-9b-it",
- "compound-beta",
- "compound-beta-mini",
- "compound-beta-oss",
- "distil-whisper-large-v3-en", # depricated
- "llama-3.1-8b-instant",
- "llama-3.3-70b-versatile",
- "llama3-70b-8192", # depricated
- "llama3-8b-8192", # depricated
- "meta-llama/llama-4-maverick-17b-128e-instruct",
- "meta-llama/llama-4-scout-17b-16e-instruct",
- "meta-llama/llama-guard-4-12b",
- "meta-llama/llama-prompt-guard-2-22m",
- "meta-llama/llama-prompt-guard-2-86m",
- "moonshotai/kimi-k2-instruct",
- "openai/gpt-oss-20b",
- "openai/gpt-oss-120b",
- "whisper-large-v3",
- "whisper-large-v3-turbo",
- "playai-tts",
- "playai-tts-arabic",
(see actual models at the [Groq API](https://github.com/groq/groq-python/) or [console.groq.com](https://console.groq.com))  

The API response:
- Normal mode: multistring literal (stream=`False`),
- JSON mode: JSON file (stream=`False` and response_format=`{'type': 'json_object'}`),
- Stream mode: stream output (stream=`True`).

### Normal mode

```python

import requests

HOST = "your_IP_adress"
PORT = 5555
URL = f"http://{HOST}:{PORT}/"

prompt = "Hello World!"

# Set the dictionary for Groq API parametres
groq_api_params = {
    "YOUR_SECRET_GROQ_TOKEN": {
        "MODEL": "llama-3.3-70b-versatile",
        "MESSAGES": [{"role": "user", "content": prompt}],
        "TEMPERATURE": 1,
        "MAX_COMPLETION_TOKENS": 1024,
        "TOP_P": 1,
        "STREAM": False,
        "STOP": None,
    }
}

# Send a POST request to the API
response = requests.post(URL, json=groq_api_params)

# Check if the request was successful
if response.status_code == 200:
    response = response.text[1:-1]
    response = response.replace('\\"', '"')
    response = response.replace('\\n', '\n')
    print(response)
else:
    print("Error:", response.status_code)
```

Output:
```
> Hello. It's nice to meet you. Is there something I can help you with, or would you like to chat?
```

### JSON mode

```python
import requests

HOST = "your_IP_adress"
PORT = 5555
URL = f"http://{HOST}:{PORT}/"

# Set the dictionary for Groq API parametres
groq_api_params = {
    "YOUR_SECRET_GROQ_TOKEN": {
        "MODEL": "llama-3.3-70b-versatile",
        "MESSAGES": list(),
        "TEMPERATURE": 1,
        "MAX_COMPLETION_TOKENS": 1024,
        "TOP_P": 1,
        "STREAM": False,
        "RESPONSE_FORMAT": {'type': 'json_object'},
        "STOP": None,
    }
}

# Add system prompt
groq_api_params["YOUR_SECRET_GROQ_TOKEN"]["MESSAGES"].append({'role' : 'system',
                                    'content' : 'Always return me json, that looks like a:\
                                               {"ANSWER": text string with your message}'})

# Add prompt
groq_api_params["YOUR_SECRET_GROQ_TOKEN"]["MESSAGES"].append({'role' : 'user',
                                    'content' : 'Hello World!'})

# Send a POST request to the API
response = requests.post(URL, json=groq_api_params)

# Check if the request was successful
if response.status_code == 200:
    response = response.text[1:-1]
    response = response.replace('\\"', '"')
    response = response.replace('\\n', '\n')
    print(response)
else:
    print("Error:", response.status_code)
```

Output (JSON):
```
{
   "ANSWER": "Hello, welcome to our conversation, how can I assist you today?"
}
```

### Stream mode

```python
import requests

HOST = "your_IP_adress"
PORT = 5555
URL = f"http://{HOST}:{PORT}/"

prompt = "Hello World!"

# Set the dictionary for Groq API parametres
groq_api_params = {
    "YOUR_SECRET_GROQ_TOKEN": {
        "MODEL": "llama-3.3-70b-versatile",
        "MESSAGES": [{"role": "user", "content": prompt}],
        "TEMPERATURE": 1,
        "MAX_COMPLETION_TOKENS": 1024,
        "TOP_P": 1,
        "STREAM": True,
        "STOP": None,
    }
}

# Send a POST request to the API
response = requests.post(URL, json=groq_api_params, stream=True)

# Check if the request was successful
if response.status_code == 200:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            print(chunk.decode("utf-8"))
else:
    print("Error:", response.status_code)
```

Output (stream):
```
>Hello
>.
> It
>'s
> nice
> to
> meet
> you
>.
> Is
> there
> something
> I
> can
> help
> you
> with
>,
> or
> would
> you
> like
> to
> chat
>?
```
