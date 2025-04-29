from sqlmodel import Session, select
from .meta.sql_db_schema import engine, Guide

def get_session():
    with Session(engine) as session:
        yield session

def get_guides(session: Session):
    return session.exec(select(Guide)).all()
