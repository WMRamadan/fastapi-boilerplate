"""App configuration."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from typing import List
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings class.
    """
    SQLALCHEMY_DATABASE_URL: str
    MONGODB_URL: str
    MONGODB_NAME: str
    CELERY_CONF_BROKER_URL: str
    CELERY_CONF_RESULT_BACKEND: str
    ALLOWED_ORIGINS: List[str]
    ALLOW_CREDENTIALS: bool
    ALLOW_METHODS: List[str]
    ALLOW_HEADERS: List[str]
    APP_DEBUG: bool

    class Config:
        """
        Config class.
        """
        env_file = ".env.example"
        env_file_encoding = 'utf-8'
