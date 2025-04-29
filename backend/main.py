from fastapi import FastAPI, Depends
from sqlmodel import Session
from database.src.meta.sql_db_schema import Guide
from database.src.sqlite3_db import get_session, get_guides

app = FastAPI()

@app.get("/api/v1/guides/")
async def get_guides():
    return {"message", "Hello from FastAPI /api/v1/guides/"}

@app.get("/")
async def get_root():
    return {"message", "Hello from FastAPI /"}