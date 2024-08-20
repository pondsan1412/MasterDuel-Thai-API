# src/meta.py
from fastapi import APIRouter

meta_router = APIRouter()

@meta_router.get("/")
def get_meta():
    return {"message": "This is the meta endpoint"}
