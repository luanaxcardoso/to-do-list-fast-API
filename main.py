from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime


import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
    with open('database.json') as f:
        data = json.load(f)
    return templates.TemplateResponse("todo_list.html", {"request": request, "tododict": data})

@app.get("/delete/{id}")
async def delete_todo(request: Request, id: str):
    with open('database.json') as f:
        data = json.load(f)
    del data[id]
    with open('database.json', 'w') as f:
        json.dump(data, f)
    return RedirectResponse("/", 303)

@app.post("/add")
async def add_todo(request: Request, data: str = Form(...), hora: str = Form(...), dia: str = Form(...), tarefa: str = Form(...)):
    
    data_formatada = datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")
    
    with open('database.json') as f:
        data_json = json.load(f)
    
    formdata = {"data": data_formatada, "hora": hora, "dia": dia, "tarefa": tarefa}
    newdata = {}
    i = 1
    for id in data_json:
        newdata[str(i)] = data_json[id]
        i += 1
    newdata[str(i)] = formdata
    with open('database.json', 'w') as f:
        json.dump(newdata, f)
    return RedirectResponse("/", 303)
