from fastapi import FastAPI

app = FastAPI(title="AI code Review Agent")

@app.get("/")
def home():
    return {"message": "Welcome to the AI code Review Agent!"}