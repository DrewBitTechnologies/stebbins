from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/")
async def get():
    return {"message", "Hello from FastAPI /api/v1/"}

@app.get("/")
async def get():
    return {"message", "Hello from FastAPI /"}