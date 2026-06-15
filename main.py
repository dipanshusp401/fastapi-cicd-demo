import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Docker!"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "mongo_url": os.getenv("MONGO_URL"),
        "redis_url": os.getenv("REDIS_URL")
    }