def test_create_customer(client):
    response = client.post(
        "/customers/", json={"first_name": "Sam", "last_name": "Lee"}
    )
    assert response.status_code == 200
    assert response.json()["first_name"] == "Sam"


def test_list_customers(client, a_customer):
    response = client.get("/customers/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_customer(client, a_customer):
    response = client.get(f"/customers/{a_customer['customer_id']}")
    assert response.status_code == 200


def test_get_customer_not_found(client):
    response = client.get("/customers/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Customer Not Found"


def test_update_customer(client, a_customer):
    response = client.put(
        f"/customers/{a_customer['customer_id']}", json={"loyalty_points": 50}
    )
    assert response.status_code == 200
    assert response.json()["loyalty_points"] == 50


def test_update_customer_not_found(client):
    response = client.put("/customers/99999", json={"loyalty_points": 5})
    assert response.status_code == 404


def test_delete_customer(client, a_customer):
    response = client.delete(f"/customers/{a_customer['customer_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Customer deleted"


def test_delete_customer_not_found(client):
    response = client.delete("/customers/99999")
    assert response.status_code == 404
