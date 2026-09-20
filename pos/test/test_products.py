import pytest
from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

@pytest.fixture
def clean_product_fixture():

    create_payload = {
        "barcode": "999888777",
        "name": "Temporary Test Product",
        "category_id": 1,
        "price": "12.50"
    }
    response = client.post("/products/", json=create_payload)
    assert response.status_code == 200
    return response.json()


def test_list_products():
    response = client.get('/products/')
    assert response.status_code == 200


def test_update_product_success(clean_product_fixture):
    product_id = clean_product_fixture["product_id"]
    update_payload = {
        "name": "Fanta",
        "price": "19.99"
    }
    response = client.put(f"/products/{product_id}", json=update_payload)
    
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == "Fanta"
    assert response_data["price"] == "19.99"


def test_update_product_not_found():
    response = client.put("/products/99999", json={"name": "Ghost Product"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Product Not Found"


def test_delete_product_success(clean_product_fixture):
    product_id = clean_product_fixture["product_id"]
    
    delete_response = client.delete(f"/products/{product_id}")
    assert delete_response.status_code == 204
    assert delete_response.text == "" 
    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404


def test_delete_product_not_found():
    response = client.delete("/products/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product Not Found"

