from fastapi import FastAPI

from app.api.review import router as review_router
from app.api.history import router as history_router

app = FastAPI(title="AI code Review Agent")

app.include_router(review_router)
app.include_router(history_router)

@app.get("/")
def home():
    return {"message": "Welcome to the AI code Review Agent!"}