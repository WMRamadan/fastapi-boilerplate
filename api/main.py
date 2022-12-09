from fastapi import FastAPI
from .routers import users, items
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Hello to the FastAPI Boilerplate!"}
