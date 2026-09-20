def test_create_sale_item(client, a_sale, a_product):
    response = client.post(
        "/sale-items/",
        json={
            "sale_id": a_sale["sale_id"],
            "product_id": a_product["product_id"],
            "quantity": 3,
            "unit_price": "1.50",
            "total_price": "4.50",
        },
    )
    assert response.status_code == 200
    assert response.json()["quantity"] == 3


def test_list_sale_items(client, a_sale, a_product):
    client.post(
        "/sale-items/",
        json={
            "sale_id": a_sale["sale_id"],
            "product_id": a_product["product_id"],
            "quantity": 1,
            "unit_price": "1.50",
            "total_price": "1.50",
        },
    )
    response = client.get("/sale-items/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_sale_item_not_found(client):
    response = client.get("/sale-items/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Sale Item Not Found"


def test_update_sale_item(client, a_sale, a_product):
    created = client.post(
        "/sale-items/",
        json={
            "sale_id": a_sale["sale_id"],
            "product_id": a_product["product_id"],
            "quantity": 1,
            "unit_price": "1.50",
            "total_price": "1.50",
        },
    ).json()
    response = client.put(
        f"/sale-items/{created['sale_item_id']}", json={"quantity": 5}
    )
    assert response.status_code == 200
    assert response.json()["quantity"] == 5


def test_update_sale_item_not_found(client):
    response = client.put("/sale-items/99999", json={"quantity": 5})
    assert response.status_code == 404


def test_delete_sale_item(client, a_sale, a_product):
    created = client.post(
        "/sale-items/",
        json={
            "sale_id": a_sale["sale_id"],
            "product_id": a_product["product_id"],
            "quantity": 1,
            "unit_price": "1.50",
            "total_price": "1.50",
        },
    ).json()
    response = client.delete(f"/sale-items/{created['sale_item_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Sale item deleted"


def test_delete_sale_item_not_found(client):
    response = client.delete("/sale-items/99999")
    assert response.status_code == 404
