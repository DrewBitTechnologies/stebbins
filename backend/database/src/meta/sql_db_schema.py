from sqlmodel import Field, Session, SQLModel, create_engine, select
from .db_bootstrap import types, colors, seasons, guides

# Define your models to match existing tables
class GuideType(SQLModel, table=True):
    __tablename__ = "guide_type"
    
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

class GuideColor(SQLModel, table=True):
    __tablename__ = "guide_color"
    
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

class GuideSeason(SQLModel, table=True):
    __tablename__ = "guide_season"
    
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

class Guide(SQLModel, table=True):
    __tablename__ = "guide"
    
    id: int | None = Field(default=None, primary_key=True)
    common_name: str = Field(default="common_name")
    latin_name: str = Field(default="latin_name")
    description: str = Field(default="description")
    modified: int = Field(default=0)
    type_id: int | None = Field(default=None, foreign_key="guide_type.id")
    color_id: int | None = Field(default=None, foreign_key="guide_color.id")
    season_id: int | None = Field(default=None, foreign_key="guide_season.id")

class GuideImage(SQLModel, table=True):
    __tablename__ = "guide_image"
    
    id: int | None = Field(default=None, primary_key=True)
    guide_id: int = Field(foreign_key="guide.id")
    path: str
    modified: int

sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///../../data/db/{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():  
    SQLModel.metadata.create_all(engine)  

def create_guide_types():

    with Session(engine) as session:
        for type in types:
            session.add(GuideType(name=type))

        session.commit()

def create_guide_colors():
    
    with Session(engine) as session:
        for color in colors:
            session.add(GuideColor(name=color))

        session.commit()

def create_guide_seasons():

    with Session(engine) as session:
        for season in seasons:
            session.add(GuideSeason(name=season))

        session.commit()

def create_guides():
    with Session(engine) as session:
        for guide in guides:
            session.add(Guide(common_name=guide["common name"],
                               latin_name=guide["latin name"], 
                               description=guide["description"]
                               ))
            session.commit()

def select_guides():
    with Session(engine) as session:
        guides = session.exec(select(Guide)).all()
        print(guides)

def create_guide_tables():
    create_guide_types()
    create_guide_seasons()
    create_guide_colors()
    create_guides()

def main():
    create_db_and_tables()
    create_guide_tables()

if __name__ == "__main__":  
    main() 