from fastapi import FastAPI
from src.webhook.github_webhook import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI Code Review Assistant Running"}