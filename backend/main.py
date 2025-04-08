from fastapi import APIRouter, File, UploadFile
from typing import List
from pydantic import BaseModel
from database.src.sqlite3_db import Sqlite3db

mobile_router = APIRouter(prefix="/setbbins/mobile/api/v1", tags=["Mobile"])
admin_router = APIRouter(prefix="/stebbins/admin/api/v1", tags=["Admin"])

db = Sqlite3db()

app = FastAPI()

@mobile_router.get("/updates/")
async def get_updates(last_update: str | None):
    pass


class ReserveReport(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    email: str
    report_text: str

@mobile_router.post("/report/")
async def post_report(report: ReserveReport, report_images: List[UploadFile] = File(...)):
    pass

@admin_router.get("/images/")
async def get_images(screen: str, tag: str):
    pass

@admin_router.get("/text/")
async def get_text(screen: str, field: str):
    pass

@admin_router.put("/images/")
async def update_image(screen: str, tag: str):
    pass

@admin_router.put("/text/")
async def update_text(screen: str, field: str):
    pass

app.include_router(mobile_router)
app.include_router(admin_router)