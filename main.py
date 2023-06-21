from fastapi import FastAPI
from enum import Enum
from fastapi.responses import FileResponse
#uvicorn main:app --reload    с помощью этого кода можно запустить фаст
app = FastAPI()
class ModelName(str, Enum):
    pidoras = "pidoras"
    pidorito = "pidorito"
    danya = 'pidor'
    
@app.get("/models/{какой ты пидорас}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.pidoras:
        return {"model_name": model_name, "danya": "Ах ты жалкий пидорас!"}
    
    if model_name.value == "pidorito":
        return {"model_name": model_name, "danya": "Ах ты жалкий пидорито!"}
    
    return {"model_name": model_name, "danya": "Ах ты жалкий пидорас Даня!"}


@app.get("/")
async def read_users():
    return ["это я просто тренировался :)  - http://127.0.0.1:8000/items/cam_pidoras"]
@app.get("/cam_pidoras")
async def read_users2():
    return ["я непидорас"]


@app.get('/danya_ne_pidor')
def read_root():
    return FileResponse('/public/index.html')
@app.get('/about.html')
def read_root():
    return FileResponse('/public/about.html')