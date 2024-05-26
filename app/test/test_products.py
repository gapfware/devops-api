import uuid
import math
from app.test.conftest import client

endpoint = "/api/v1/products"

def test_read_products():
    response = client.get(endpoint)
    assert response.status_code == 200
    if response.json() == []:
        assert response.json() == []
    else:
        assert isinstance(response.json()[0]["id"], int)
        assert isinstance(response.json()[0]["name"], str)
        assert isinstance(response.json()[0]["unique_name"], str)
        assert isinstance(response.json()[0]["category_id"], int)
        assert isinstance(response.json()[0]["min_amount"], int)
        assert isinstance(response.json()[0]["existence"], int)
        assert isinstance(response.json()[0]["price_unit_usd"], float | int)
        assert isinstance(response.json()[0]["price_unit_pesos"], float | int)
        assert isinstance(response.json()[0]["description"], str)


def test_create_product():
    response = client.post(endpoint, json={
        "name": "Test Product",
        "unique_name": f"Test Unique Name {uuid.uuid4()}",
        "category_id": 1,
        "min_amount": 1,
        "existence": 1,
        "price_unit_usd": 1.0,
        "price_unit_pesos": 1.0,
        "description": "Test Description"
    })
    assert response.status_code == 201
    assert isinstance(response.json()["id"], int)
    assert response.json()["name"] == "Test Product"
    assert isinstance(response.json()["unique_name"], str)
    assert response.json()["category_id"] == 1
    assert response.json()["min_amount"] == 1
    assert response.json()["existence"] == 1
    assert math.isclose(response.json()["price_unit_pesos"], 1.0)
    assert math.isclose(
        response.json()["price_unit_pesos"], 1.0, rel_tol=1e-09, abs_tol=1e-09)
    assert response.json()["description"] == "Test Description"


def test_create_product_repeated_unique_name():
    unique_name = f"Test Unique Name {uuid.uuid4()}"
    response = client.post(endpoint, json={
        "name": "Test Product",
        "unique_name": unique_name,
        "category_id": 1,
        "min_amount": 1,
        "existence": 1,
        "price_unit_usd": 1.0,
        "price_unit_pesos": 1.0,
        "description": "Test Description"
    })
    assert response.status_code == 201
    response = client.post(endpoint, json={
        "name": "Test Product",
        "unique_name": unique_name,
        "category_id": 1,
        "min_amount": 1,
        "existence": 1,
        "price_unit_usd": 1.0,
        "price_unit_pesos": 1.0,
        "description": "Test Description"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Product unique name already exists"}


def test_read_product_by_id():
    response = client.get(endpoint)
    assert response.status_code == 200
    if response.json() == []:
        assert response.json() == []
    else:
        product_id = response.json()[0]["id"]
        response = client.get(f"{endpoint}/{product_id}")
        assert response.status_code == 200
        assert response.json()["id"] == product_id
        assert isinstance(response.json()["name"], str)
        assert isinstance(response.json()["unique_name"], str)
        assert isinstance(response.json()["category_id"], int)
        assert isinstance(response.json()["min_amount"], int)
        assert isinstance(response.json()["existence"], int)
        assert isinstance(response.json()["price_unit_usd"], float | int)
        assert isinstance(response.json()["price_unit_pesos"], float | int)
        assert isinstance(response.json()["description"], str)


def test_read_product_by_id_not_found():
    response = client.get(endpoint)
    assert response.status_code == 200
    if response.json() == []:
        assert response.json() == []
    else:
        product_id = response.json()[-1]["id"]
        response = client.get(f"{endpoint}/{product_id + 1}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Product not found"}


def test_update_product():
    response = client.get(endpoint)
    assert response.status_code == 200
    if response.json() == []:
        assert response.json() == []
    else:
        product_id = response.json()[0]["id"]
        response = client.put(f"{endpoint}/{product_id}", json={
            "name": "Test Product",
            "unique_name": f"Test Unique Name {uuid.uuid4()}",
            "category_id": 1,
            "min_amount": 1,
            "existence": 1,
            "price_unit_usd": 1.0,
            "price_unit_pesos": 1.0,
            "description": "Test Description"
        })
        assert response.status_code == 200
        assert response.json()["id"] == product_id
        assert response.json()["name"] == "Test Product"
        assert isinstance(response.json()["unique_name"], str)
        assert response.json()["category_id"] == 1
        assert response.json()["min_amount"] == 1
        assert response.json()["existence"] == 1
        assert math.isclose(response.json()["price_unit_pesos"], 1.0)
        assert math.isclose(
            response.json()["price_unit_pesos"], 1.0, rel_tol=1e-09, abs_tol=1e-09)
        assert response.json()["description"] == "Test Description"


def test_delete_product():
    response = client.get(endpoint)
    assert response.status_code == 200
    if response.json() == []:
        assert response.json() == []
    else:
        product_id = response.json()[0]["id"]
        response = client.delete(f"{endpoint}/{product_id}")
        assert response.status_code == 200
        assert response.json()["id"] == product_id
        response = client.get(f"{endpoint}/{product_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Product not found"}
