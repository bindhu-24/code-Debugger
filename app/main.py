from fastapi import FastAPI

from app.api.review import router as review_router

app = FastAPI(title="AI code Review Agent")

app.include_router(review_router)

@app.get("/")
def home():
    return {"message": "Welcome to the AI code Review Agent!"}