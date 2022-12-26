"""Application main."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
import os
from functools import lru_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from api.routers import async_router, users, items, tasks, stream
from . import database, config

database.Base.metadata.create_all(bind=database.engine)

@lru_cache()
def get_settings():
    """
    Config settings function.
    """
    return config.Settings()

conf_settings = get_settings()

app = FastAPI(debug=conf_settings.APP_DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=conf_settings.ALLOWED_ORIGINS,
    allow_credentials=conf_settings.ALLOW_CREDENTIALS,
    allow_methods=conf_settings.ALLOW_METHODS,
    allow_headers=conf_settings.ALLOW_HEADERS,
)
app.include_router(async_router.router)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(tasks.router)
app.include_router(stream.router)

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
