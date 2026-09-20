def make_payment_payload(a_sale, a_supplier, **overrides):
    payload = dict(
        sale_id=a_sale["sale_id"],
        supplier_id=a_supplier["supplier_id"],
        payment_method="cash",
        amount_paid="11.00",
        change_given="0.00",
        transaction_reference=None,
        paid_at="2026-01-01T12:00:00Z",
    )
    payload.update(overrides)
    return payload


def test_create_payment(client, a_sale, a_supplier):
    response = client.post(
        "/payments/", json=make_payment_payload(a_sale, a_supplier)
    )
    assert response.status_code == 200
    assert response.json()["payment_method"] == "cash"


def test_list_payments(client, a_sale, a_supplier):
    client.post("/payments/", json=make_payment_payload(a_sale, a_supplier))
    response = client.get("/payments/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_payment_not_found(client):
    response = client.get("/payments/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Payment Not Found"


def test_update_payment(client, a_sale, a_supplier):
    created = client.post(
        "/payments/", json=make_payment_payload(a_sale, a_supplier)
    ).json()
    response = client.put(
        f"/payments/{created['payment_id']}", json={"payment_method": "card"}
    )
    assert response.status_code == 200
    assert response.json()["payment_method"] == "card"


def test_update_payment_not_found(client):
    response = client.put("/payments/99999", json={"payment_method": "card"})
    assert response.status_code == 404


def test_delete_payment(client, a_sale, a_supplier):
    created = client.post(
        "/payments/", json=make_payment_payload(a_sale, a_supplier)
    ).json()
    response = client.delete(f"/payments/{created['payment_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Payment deleted"


def test_delete_payment_not_found(client):
    response = client.delete("/payments/99999")
    assert response.status_code == 404
