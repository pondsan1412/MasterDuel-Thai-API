# src/packcard.py
from fastapi import APIRouter

packcard_router = APIRouter()

@packcard_router.get("/")
def get_packcard():
    return {"message": "This is the packcard endpoint"}
