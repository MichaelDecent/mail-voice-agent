from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.voice import router as voice_router

app = FastAPI(title="Voice Mail Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voice_router, prefix="/voice")


@app.get("/")
async def root():
    return {"status": "ok"}
