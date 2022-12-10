"""Application main."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from fastapi import FastAPI
from loguru import logger
from api.routers import users, items, tasks
from . import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)
app.include_router(tasks.router)

logger.add("log_api.log", rotation="100 MB")    # Automatically rotate log file


@app.get("/")
async def root():
    """
    Root router.
    """
    logger.info("this is a info line")
    return {"message": "Hello to the FastAPI Boilerplate!"}
