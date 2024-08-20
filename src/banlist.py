# src/banlist.py
from fastapi import APIRouter

banlist_router = APIRouter()

@banlist_router.get("/")
def get_banlist():
    return {"message": "This is the banlist endpoint"}
