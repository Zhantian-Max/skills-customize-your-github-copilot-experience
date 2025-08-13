from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items = [
    {"name": "Libro", "price": 12.5},
    {"name": "Cuaderno", "price": 3.0},
    {"name": "Lápiz", "price": 0.5}
]

@app.get("/items")
def get_items() -> List[dict]:
    return items

@app.post("/items")
def add_item(item: Item) -> dict:
    new_item = item.dict()
    items.append(new_item)
    return new_item
