def test_create_sale(client, a_user, a_customer):
    response = client.post(
        "/sales/",
        json={
            "customer_id": a_customer["customer_id"],
            "user_id": a_user["user_id"],
            "subtotal": "20.00",
            "tax_amount": "2.00",
            "discount_amount": "0.00",
            "grand_total": "22.00",
            "status": "completed",
        },
    )
    assert response.status_code == 200
    assert response.json()["status"] == "completed"


def test_create_sale_without_customer(client, a_user):
    response = client.post(
        "/sales/",
        json={
            "user_id": a_user["user_id"],
            "subtotal": "5.00",
            "tax_amount": "0.50",
            "discount_amount": "0.00",
            "grand_total": "5.50",
            "status": "completed",
        },
    )
    assert response.status_code == 200
    assert response.json()["customer_id"] is None


def test_list_sales(client, a_sale):
    response = client.get("/sales/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_sale(client, a_sale):
    response = client.get(f"/sales/{a_sale['sale_id']}")
    assert response.status_code == 200


def test_get_sale_not_found(client):
    response = client.get("/sales/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Sale Not Found"


def test_update_sale(client, a_sale):
    response = client.put(f"/sales/{a_sale['sale_id']}", json={"status": "refunded"})
    assert response.status_code == 200
    assert response.json()["status"] == "refunded"


def test_update_sale_not_found(client):
    response = client.put("/sales/99999", json={"status": "refunded"})
    assert response.status_code == 404


def test_delete_sale(client, a_sale):
    response = client.delete(f"/sales/{a_sale['sale_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Sale deleted"


def test_delete_sale_not_found(client):
    response = client.delete("/sales/99999")
    assert response.status_code == 404
