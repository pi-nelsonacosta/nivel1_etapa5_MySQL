import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.auth import create_access_token
from app.models.user import User

client = TestClient(app)

@pytest.fixture
def test_user():
    return User(email="testuser@example.com", is_active=True, is_superuser=False)

@pytest.fixture
def auth_token(test_user):
    return create_access_token(test_user.email)  # Cambiado a 'email'

def test_create_user():
    response = client.post(
        "/user/register",
        json={"email": "testuser@example.com", "password": "newpassword"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"




