# src/top_deck.py
from fastapi import APIRouter

top_deck_router = APIRouter()

@top_deck_router.get("/")
def get_top_deck():
    return {"message": "This is the top_deck endpoint"}
