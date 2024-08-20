# src/card.py
from fastapi import APIRouter

card_router = APIRouter()

@card_router.get("/")
def get_card():
    return {"message": "This is the card endpoint"}
