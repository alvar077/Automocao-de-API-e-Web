import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest
from utils.api_client import get, post, put, delete

USERNAME = "testuser_auto"

USER_PAYLOAD = {
    "id": 999,
    "username": USERNAME,
    "firstName": "Test",
    "lastName": "User",
    "email": "test@email.com",
    "password": "senha123",
    "phone": "11999999999",
    "userStatus": 1
}


def test_create_user():
    response = post("/user", USER_PAYLOAD)
    assert response.status_code == 200

def test_get_user():
    response = get(f"/user/{USERNAME}")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == USERNAME

def test_update_user():
    updated = USER_PAYLOAD.copy()
    updated["firstName"] = "Updated"
    response = put(f"/user/{USERNAME}", updated)
    assert response.status_code == 200

def test_login_user():
    response = get(f"/user/login?username={USERNAME}&password=senha123")
    assert response.status_code == 200

def test_logout_user():
    response = get("/user/logout")
    assert response.status_code == 200

def test_delete_user():
    response = delete(f"/user/{USERNAME}")
    assert response.status_code == 200

def test_get_deleted_user_returns_404():
    response = get(f"/user/{USERNAME}")
    assert response.status_code == 404
