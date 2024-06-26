import uuid
from app.test.conftest import client

endpoint = "/api/v1/categories"

def test_read_categories():

    response = client.get(endpoint)
    assert response.status_code == 200
    if response.json() == []:
        assert response.json() == []
    else:
        assert isinstance(response.json()[0]["id"], int)
        assert isinstance(response.json()[0]["name"], str)
        assert isinstance(response.json()[0]["measures"], str)
        assert isinstance(response.json()[0]["allows"], str)
        assert isinstance(response.json()[0]["others"], dict)


def test_read_category_by_id():
    response = client.get(endpoint)
    assert response.status_code == 200
    if response.json() == []:
        assert response.json() == []
    else:
        category_id = response.json()[0]["id"]
        response = client.get(f"{endpoint}/{category_id}")
        assert response.status_code == 200
        assert response.json()["id"] == category_id
        assert isinstance(response.json()["name"], str)
        assert isinstance(response.json()["measures"], str)
        assert isinstance(response.json()["allows"], str)
        assert isinstance(response.json()["others"], dict)


def test_create_category():
    name = f"Test Category {uuid.uuid4()}"
    response = client.post(
        endpoint,
        json={
            "name": name,
            "measures": "Test Measures",
            "allows": "Test Allows",
            "others": {"test": "test"}
        }
    )
    assert response.status_code == 201
    assert isinstance(response.json()["id"], int)
    assert response.json()["name"] == name
    assert response.json()["measures"] == "Test Measures"
    assert response.json()["allows"] == "Test Allows"
    assert response.json()["others"] == {"test": "test"}


def test_create_category_repeated_name():
    name = f"Test Category {uuid.uuid4()}"
    response = client.post(
        endpoint,
        json={
            "name": name,
            "measures": "Test Measures",
            "allows": "Test Allows",
            "others": {"test": "test"}
        }
    )
    assert response.status_code == 201

    response = client.post(
        endpoint,
        json={
            "name": name,
            "measures": "Test Measures",
            "allows": "Test Allows",
            "others": {"test": "test"}
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Category already exists"}


def test_update_category():
    name = f"Test Category update {uuid.uuid4()}"
    response = client.post(
        endpoint,
        json={
            "name": name,
            "measures": "Test Measures",
            "allows": "Test Allows",
            "others": {"test": "test"}
        }
    )
    assert response.status_code == 201

    category_id = response.json()["id"]
    response = client.put(
        f"{endpoint}/{category_id}",
        json={
            "name": name,
            "measures": "Test Measures Updated",
            "allows": "Test Allows Updated",
            "others": {"test": "test"}
        }
    )
    assert response.status_code == 200
    assert response.json()["measures"] == "Test Measures Updated"
    assert response.json()["allows"] == "Test Allows Updated"


def test_delete_category():
    name = f"Test Category delete {uuid.uuid4()}"
    response = client.post(
        endpoint,
        json={
            "name": name,
            "measures": "Test Measures",
            "allows": "Test Allows",
            "others": {"test": "test"}
        }
    )
    assert response.status_code == 201

    category_id = response.json()["id"]

    response = client.delete(f"{endpoint}/{category_id}")
    assert response.status_code == 200
    assert isinstance(response.json()["id"], int)
    assert response.json()["name"] == name
    assert response.json()["measures"] == "Test Measures"
    assert response.json()["allows"] == "Test Allows"
    assert response.json()["others"] == {"test": "test"}
