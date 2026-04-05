"""Tests for the main FastAPI application."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
import pytest
from fastapi.testclient import TestClient

from api import main
from api.database import get_db
from api.tests.db import Base, engine, override_get_db


@pytest.fixture(autouse=True)
def setup_database():
    """Create a fresh schema for each test."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client():
    """Provide a test client using the overridden database dependency."""
    main.app.dependency_overrides[get_db] = override_get_db
    test_client = TestClient(main.app)
    yield test_client
    test_client.close()
    main.app.dependency_overrides.clear()


def _create_user(client: TestClient, email: str = "testing@email.com"):
    """Create a user through the API."""
    return client.post(
        "/users/",
        json={"email": email, "password": "testpwd123"},
    )


def test_root(client: TestClient):
    """Test root route."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from the FastAPI Boilerplate!"}


def test_health(client: TestClient):
    """Test health route."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "info": main.get_info()}


def test_create_user(client: TestClient):
    """Test user creation."""
    response = _create_user(client)

    assert response.status_code == 200
    assert response.json() == {
        "email": "testing@email.com",
        "id": 1,
        "is_active": True,
        "items": [],
        "tasks": [],
    }


def test_get_users(client: TestClient):
    """Test listing users."""
    create_response = _create_user(client)
    response = client.get("/users/")

    assert create_response.status_code == 200
    assert response.status_code == 200
    assert response.json() == [
        {
            "email": "testing@email.com",
            "id": 1,
            "is_active": True,
            "items": [],
            "tasks": [],
        }
    ]
