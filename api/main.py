"""Application main."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
import time
import asyncio
from fastapi import FastAPI
from loguru import logger
from api.routers import users, items, tasks
from api.helpers import async_helper
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
    start = time.time()
    a,b = await asyncio.gather(*[async_helper.async_func_a(2), async_helper.async_func_b(4)])
    end = time.time()
    result = {
        "message": "Hello from the FastAPI Boilerplate!",
        "async_func_a": a,
        "async_func_b": b,
        "async_total_time": "All functions took {} seconds.".format(round(end-start))
    }
    return result
