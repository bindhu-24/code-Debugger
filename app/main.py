from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import Base, engine
import app.database.models

from app.api.review import router as review_router
from app.api.history import router as history_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))

    Base.metadata.create_all(bind=engine)

    print("Database tables created successfully.")

    yield


app = FastAPI(
    title="AI Code Review Agent",
    lifespan=lifespan
)

app.include_router(review_router)
app.include_router(history_router)


@app.get("/")
def home():
    return {"message": "Welcome to the AI Code Review Agent!"}

@app.get("/health")
def health():
    return {"status": "healthy"}