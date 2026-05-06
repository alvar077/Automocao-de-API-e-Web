import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest
from utils.api_client import get, post, put, delete

PET_ID = 123456789

PET_PAYLOAD = {
    "id": PET_ID,
    "name": "Rex",
    "status": "available",
    "photoUrls": ["http://example.com/photo.jpg"],
    "category": {"id": 1, "name": "Dogs"},
    "tags": [{"id": 1, "name": "friendly"}]
}


def test_create_pet():
    response = post("/pet", PET_PAYLOAD)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Rex"

def test_get_pet_by_id():
    response = get(f"/pet/{PET_ID}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == PET_ID

def test_update_pet():
    updated = PET_PAYLOAD.copy()
    updated["name"] = "Rex Updated"
    response = put("/pet", updated)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Rex Updated"

def test_find_pets_by_status():
    response = get("/pet/findByStatus?status=available")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_delete_pet():
    response = delete(f"/pet/{PET_ID}")
    assert response.status_code == 200

def test_get_deleted_pet_returns_404():
    response = get(f"/pet/{PET_ID}")
    assert response.status_code == 404
