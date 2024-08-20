# src/main.py
from fastapi import FastAPI
from src.card import card_router
from src.packcard import packcard_router
from src.banlist import banlist_router
from src.top_deck import top_deck_router
from src.meta import meta_router

app = FastAPI()

@app.get("/")
async def root():
    return {
        "masterduel_api":{
            "author": "Satorn Sukkang",
            "version": 1.0,
            "doc": None,
            "project url" : "https://github.com/pondsan1412/MasterDuel-Thai-API",
            "contributor": ["pondsan1412",]
            
        }
    }


app.include_router(card_router, prefix="/card", tags=["card"])
app.include_router(packcard_router, prefix="/packcard", tags=["packcard"])
app.include_router(banlist_router, prefix="/banlist", tags=["banlist"])
app.include_router(top_deck_router, prefix="/top_deck", tags=["top_deck"])
app.include_router(meta_router, prefix="/meta", tags=["meta"])
