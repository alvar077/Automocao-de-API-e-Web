import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest
from utils.api_client import get, post, delete

ORDER_ID = 5

ORDER_PAYLOAD = {
    "id": ORDER_ID,
    "petId": 1,
    "quantity": 2,
    "shipDate": "2024-01-01T00:00:00.000Z",
    "status": "placed",
    "complete": True
}


def test_get_inventory():
    response = get("/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_place_order():
    response = post("/store/order", ORDER_PAYLOAD)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == ORDER_ID

def test_get_order_by_id():
    response = get(f"/store/order/{ORDER_ID}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "placed"

def test_delete_order():
    response = delete(f"/store/order/{ORDER_ID}")
    assert response.status_code == 200

def test_get_deleted_order_returns_404():
    response = get(f"/store/order/{ORDER_ID}")
    assert response.status_code == 404
