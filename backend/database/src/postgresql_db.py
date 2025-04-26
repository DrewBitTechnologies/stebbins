from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://postgres:password@db:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session