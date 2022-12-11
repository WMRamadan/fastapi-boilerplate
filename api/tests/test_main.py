"""Tests for main."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
import pytest
from fastapi.testclient import TestClient
from api.database import Base, get_db
from api import main
from api.tests.db import engine, override_get_db

@pytest.fixture()
def test_db():
    """
    Test database.
    """
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

main.app.dependency_overrides[get_db] = override_get_db

client = TestClient(main.app)

def _create_user(test_db):
    """
    Create user.
    """
    response = client.post(
        "/users/",
        # headers={"X-Token": "coneofsilence"},
        json={"email": "testing@email.com", "password": "testpwd123"},
    )
    return response

def test_root():
    """
    Test root route.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from the FastAPI Boilerplate!"}

def test_health():
    """
    Test health route.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "info": main.get_info()
        }

def test_create_user(test_db):
    """
    Test create user.
    """
    response = _create_user(test_db)
    assert response.status_code == 200
    assert response.json() == {
    "email": "testing@email.com",
    "id": 1,
    "is_active": True,
    "items": [ ],
    "tasks": [ ]
    }

def test_get_users(test_db):
    """
    Test get users.
    """
    _create_user(test_db)
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [{
    "email": "testing@email.com",
    "id": 1,
    "is_active": True,
    "items": [ ],
    "tasks": [ ]
    }]
