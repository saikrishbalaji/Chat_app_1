from fastapi import FastAPI, Form, status, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import db

app = FastAPI()
app.mount("/static", StaticFiles(directory="ui"), name="static")

template = Jinja2Templates("app/templates")

@app.get("/chat", response_class=HTMLResponse)
def get_chat():
    return template.TemplateResponse(
        "chat.html", context={"request":{}, "messages":db.get_messages(0)}
    )

@app.post('/chat/message')
def post_message(message:db.Message):
    print("123")
    print(message)
    db.set_message(message)

@app.get('/chat/{room_id}')
def get_messages(room_id:int):
    print(db.get_messages(room_id))
    return db.get_messages(room_id)