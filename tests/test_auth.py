from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import pytest

from backend.main import app
from backend.database import get_db, Base
from backend import models

# Setup the test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency override for the test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown_db():
    # Create tables before each test
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables after each test
    Base.metadata.drop_all(bind=engine)


def test_register_user():
    """
    Test user registration.
    """
    response = client.post(
        "/api/auth/register",
        json={"email": "test@example.com", "password": "password123", "name": "Test User"},
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_user():
    """
    Test user login with valid credentials after registration.
    """
    # First, register a user
    client.post(
        "/api/auth/register",
        json={"email": "testlogin@example.com", "password": "password123", "name": "Test Login"},
    )

    # Now, log in with the registered user
    response = client.post(
        "/api/auth/login",
        json={"email": "testlogin@example.com", "password": "password123"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_password():
    """
    Test user login with an invalid password.
    """
    # First, register a user
    client.post(
        "/api/auth/register",
        json={"email": "testinvalid@example.com", "password": "password123", "name": "Test Invalid"},
    )

    # Attempt to log in with the wrong password
    response = client.post(
        "/api/auth/login",
        json={"email": "testinvalid@example.com", "password": "wrongpassword"},
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] == "Incorrect email or password"

def test_register_existing_user():
    """
    Test registering a user with an email that already exists.
    """
    client.post(
        "/api/auth/register",
        json={"email": "existing@example.com", "password": "password123", "name": "Existing User"},
    )

    # Try to register again with the same email
    response = client.post(
        "/api/auth/register",
        json={"email": "existing@example.com", "password": "password456", "name": "Another User"},
    )

    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Email already registered"

