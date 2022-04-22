from time import clock_getres
from typing import List, Optional
from dataclasses import field 
from fastapi import FastAPI
import json
from pydantic.dataclasses import dataclass  

from producer import Producer
from consumer import Consumer

app = FastAPI()

PRODUCER = Producer('dog')


@dataclass
class Item:
    name: str
    description: Optional[str] = None


@app.post("/send/items/") 
async def create_author_items(items: Item):
    _dict = items.__dict__
    PRODUCER.send_message({"items": [{ "name": _dict.get('name'), "description": _dict.get("description") }] })
    return {"items": items} 



@app.get("/send/{message}")
def send_message(message: str):
    PRODUCER.send_message({ "message": message })
    return {"message": message }

