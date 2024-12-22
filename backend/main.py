from fastapi import FastAPI
from databases.database import engine
import models.product
from routers.router import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)