def test_create_supplier(client):
    response = client.post(
        "/suppliers/", json={"company_name": "Global Foods", "email": "gf@example.com"}
    )
    assert response.status_code == 200
    assert response.json()["company_name"] == "Global Foods"


def test_list_suppliers(client, a_supplier):
    response = client.get("/suppliers/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_supplier(client, a_supplier):
    response = client.get(f"/suppliers/{a_supplier['supplier_id']}")
    assert response.status_code == 200


def test_get_supplier_not_found(client):
    response = client.get("/suppliers/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Supplier Not Found"


def test_update_supplier(client, a_supplier):
    response = client.put(
        f"/suppliers/{a_supplier['supplier_id']}", json={"phone": "555-1234"}
    )
    assert response.status_code == 200
    assert response.json()["phone"] == "555-1234"


def test_update_supplier_not_found(client):
    response = client.put("/suppliers/99999", json={"phone": "555-0000"})
    assert response.status_code == 404


def test_delete_supplier(client, a_supplier):
    response = client.delete(f"/suppliers/{a_supplier['supplier_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Supplier deleted"


def test_delete_supplier_not_found(client):
    response = client.delete("/suppliers/99999")
    assert response.status_code == 404
