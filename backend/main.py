from fastapi import FastAPI
from databases.database import engine
from models import Base  # Import Base from the models package
from routers.router import router

# Create all tables defined in the models
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Product API!"}
