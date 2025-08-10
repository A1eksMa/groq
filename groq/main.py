from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uvicorn
from config import HOST, PORT
import os
import importlib

app = FastAPI()
model_router_map = {}

# Dynamically load routers and populate the model_router_map
routers_dir = os.path.join(os.path.dirname(__file__), 'routers')
for filename in os.listdir(routers_dir):
    if filename.endswith('.py') and not filename.startswith('__') and not filename.startswith('common_'):
        module_name = f"routers.{filename[:-3]}"
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, 'router'):
                # Include the router in the app
                app.include_router(module.router)
                # Populate the map for the dispatcher
                for route in module.router.routes:
                    if hasattr(route, "path"):
                        # The path is like '/model-name'. We use the name as the key.
                        model_name = route.path.lstrip('/')
                        model_router_map[model_name] = route.endpoint
        except Exception as e:
            print(f"Failed to load or map router from {filename}: {e}")

@app.post("/")
async def groq_api_dispatcher(request: Request):
    groq = await request.json()
    api_key = list(groq.keys())[0]
    model = groq[api_key].get("MODEL")

    if not model:
        raise HTTPException(status_code=400, detail="MODEL not specified in the request.")

    # Use the map for an efficient O(1) lookup
    endpoint_func = model_router_map.get(model)
    
    if not endpoint_func:
        return JSONResponse(status_code=404, content={"detail": f"Model '{model}' not found."})

    # Call the corresponding endpoint function
    return await endpoint_func(groq=groq)

if __name__=="__main__":
    uvicorn.run(app, host=HOST, port=PORT)
