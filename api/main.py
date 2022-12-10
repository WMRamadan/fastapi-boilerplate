"""Application main."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from fastapi import FastAPI
from api.routers import users, items
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)


@app.get("/")
async def root():
    """
    Root router.
    """
    return {"message": "Hello to the FastAPI Boilerplate!"}
