"""Database configuration."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./api.db"
#---------------------------------------------------------------------------------------#
# To use PostgreSQL Database comment the above line and uncomment the line below.
# Make sure to update the below settings with correct user/password and database address.
#---------------------------------------------------------------------------------------#
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

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
