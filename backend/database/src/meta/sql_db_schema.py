from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Guide(SQLModel, table=True):
    id: int = Field(default=None)
    element: int = Field(index=True, foreign_key="Guide_Element.id")
    common_name: str = Field(default="common name")
    latin_name: str = Field(default="latin name")
    description: str = Field(default="description")
