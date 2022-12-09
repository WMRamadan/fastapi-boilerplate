from . import models, database
from fastapi import FastAPI
from api.routers import users, items

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Hello to the FastAPI Boilerplate!"}
