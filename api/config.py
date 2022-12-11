"""App configuration."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings class.
    """
    SQLALCHEMY_DATABASE_URL: str

    class Config:
        """
        Config class.
        """
        env_file = ".env.example"
