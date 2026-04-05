"""Database configuration."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from . import config


@lru_cache()
def get_settings():
    """
    Config settings function.
    """
    return config.Settings()

conf_settings = get_settings()

SQLALCHEMY_DATABASE_URL = conf_settings.SQLALCHEMY_DATABASE_URL

MONGODB_URL = conf_settings.MONGODB_URL
MONGODB_NAME = conf_settings.MONGODB_NAME

mongodb_client = MongoClient(MONGODB_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    """
    Gets database session.
    """
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

def get_mongodb():
    """
    Init MongoDB Database.
    """
    mongo_db = mongodb_client[MONGODB_NAME]
    return mongo_db
