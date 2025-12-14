from fastapi.testclient import TestClient
# We are importing 'app' from main, which doesn't exist yet.
# This causes an immediate failure (Red state).
from src.main import app 

client = TestClient(app)

def test_register_user():
    payload = {
        "email": "test@example.com",
        "password": "securepassword123",
        "name": "Test User"
    }
    
    # Act: Send a POST request to register
    response = client.post("/api/auth/register", json=payload)
    
    # Assert: We expect a 201 Created status and a token in the response
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"