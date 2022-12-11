"""Application main."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from api.routers import async_router, users, items, tasks
from . import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(debug=True)
origins = [
    "http://localhost",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(async_router.router)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(tasks.router)

logger.add("log_api.log", rotation="100 MB")    # Automatically rotate log file

def get_info():
    """
    Info function.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(BASE_DIR, 'VERSION'), 'r') as fh:
        version = fh.read().strip()
    info = {
        "boilerplate_version": version,
        "fastapi_debug": app.debug
    }
    return info

@app.get("/")
async def root():
    """
    Root router.
    """
    logger.info("this is root")
    result = {
        "message": "Hello from the FastAPI Boilerplate!"
    }
    return result

@app.get("/health")
def health():
    """
    Health router.
    """
    logger.info("this is health")
    result = {
        "status": "ok",
        "info": get_info()
    }
    return result
