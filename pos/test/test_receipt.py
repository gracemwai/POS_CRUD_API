def make_receipt_payload(a_sale, **overrides):
    payload = dict(
        sale_id=a_sale["sale_id"],
        receipt_number="R-0001",
        delivery_method="printed",
        issued_at="2026-01-01T12:00:00Z",
    )
    payload.update(overrides)
    return payload


def test_create_receipt(client, a_sale):
    response = client.post("/receipts/", json=make_receipt_payload(a_sale))
    assert response.status_code == 200
    assert response.json()["receipt_number"] == "R-0001"


def test_list_receipts(client, a_sale):
    client.post("/receipts/", json=make_receipt_payload(a_sale))
    response = client.get("/receipts/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_receipt_not_found(client):
    response = client.get("/receipts/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Receipt Not Found"


def test_update_receipt(client, a_sale):
    created = client.post("/receipts/", json=make_receipt_payload(a_sale)).json()
    response = client.put(
        f"/receipts/{created['receipt_id']}", json={"delivery_method": "email"}
    )
    assert response.status_code == 200
    assert response.json()["delivery_method"] == "email"


def test_update_receipt_not_found(client):
    response = client.put("/receipts/99999", json={"delivery_method": "email"})
    assert response.status_code == 404


def test_delete_receipt(client, a_sale):
    created = client.post("/receipts/", json=make_receipt_payload(a_sale)).json()
    response = client.delete(f"/receipts/{created['receipt_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Receipt deleted"


def test_delete_receipt_not_found(client):
    response = client.delete("/receipts/99999")
    assert response.status_code == 404


def test_sale_id_must_be_unique(client, a_sale):
    import pytest
    from sqlalchemy.exc import IntegrityError

    client.post("/receipts/", json=make_receipt_payload(a_sale))
    
    with pytest.raises(IntegrityError):
        client.post(
            "/receipts/", json=make_receipt_payload(a_sale, receipt_number="R-0002")
        )
