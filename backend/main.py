from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/guide_elements")
async def get_guide_elements():
    return {"message", "Hello from FastAPI /api/v1/"}

@app.get("/")
async def get_root():
    return {"message", "Hello from FastAPI /"}