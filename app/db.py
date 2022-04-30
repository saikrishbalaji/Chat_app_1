import sqlite3
import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int = -1
    name: str = ""
    email: str
    password: str

class Room (BaseModel):
    id: int=-1
    name: str
    user: str
    messages: int=0

class Message(BaseModel):
    id: int = -1
    room_id: int = 0
    user: str
    message: str
    when: datetime.datetime = datetime.datetime.now()

DB = sqlite3.connect("app.db", check_same_thread=False)

EMPTY_MESSAGE = Message(room_id = -1, user="", message="")
EMPTY_USER = User(name="",email="", password="")
EMPTY_ROOM = Room(user="", name="")

MESSAGES: list[Message] = [
    Message(room_id = 0, user="Bill", message="Hello"),
    Message(room_id = 0, user="John", message="Hello"),
    Message(room_id = 0, user="Bill", message="How are you?"),
    Message(room_id = 0, user="John", message="Good, you?"),
    Message(room_id = 0, user="Sai", message="Hello, I made this app")]
USERS: list[User] = [
    User(name="John",email="abc@xyz.com", password="1234"),
    User(name="Bill",email="xyz@xyz.com", password="5678"),
    User(name="Sai",email="qrs@xyz.com", password="3692")]
ROOMS: list[Room] =[
    Room(user="Sai", name="Public"),
    Room(user="XYZ", name="John")]

def set_initialize():
    DB.execute(
        "CREATE TABLE IF NOT EXISTS USERS (ID INTEGER PRIMARY KEY, EMAIL STRING, NAME STRING, PASSWORD STRING);"
    )
    DB.execute(
        "CREATE TABLE IF NOT EXISTS ROOMS (ID INTEGER PRIMARY KEY, NAME STRING, USER STRING, MESSAGES INTEGER);"
    )
    DB.execute(
        "CREATE TABLE IF NOT EXISTS MESSAGES (ID INTEGER PRIMARY KEY, ROOM_ID INT, USER STRING, WHEN STRING);"
    )
    DB.commit()

def get_messages(room_id: int) -> list[Message]:
    ROOM_MESSAGES = []
    for message in MESSAGES:
        if message.room_id == room_id:
            ROOM_MESSAGES.append(message)
    return ROOM_MESSAGES

def set_message(message:Message):
    MESSAGES.append(message)
