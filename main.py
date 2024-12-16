from typing import Optional
from sqlalchemy.sql import text
from sqlmodel import Field, Session, SQLModel, create_engine

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine("sqlite:///database.db", echo=True)

# Creating session
with Session(engine) as session:
    # Query SQL
    statement = text("SELECT * FROM hero;")

    # Executing query
    results = session.exec(statement)

    # Fetch of results
    heroes = results.fetchall()
    print(heroes)