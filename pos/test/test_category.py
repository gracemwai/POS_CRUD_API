def test_create_category(client):
    response = client.post(
        "/categories/", json={"name": "Snacks", "description": "Chips and such"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Snacks"
    assert "category_id" in data


def test_list_categories(client, a_category):
    response = client.get("/categories/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_category(client, a_category):
    response = client.get(f"/categories/{a_category['category_id']}")
    assert response.status_code == 200
    assert response.json()["name"] == a_category["name"]


def test_get_category_not_found(client):
    response = client.get("/categories/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Category Not Found"


def test_update_category(client, a_category):
    response = client.put(
        f"/categories/{a_category['category_id']}", json={"name": "Cold Drinks"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Cold Drinks"


def test_update_category_not_found(client):
    response = client.put("/categories/99999", json={"name": "Ghost"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Category Not Found"


def test_delete_category(client, a_category):
    response = client.delete(f"/categories/{a_category['category_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Category deleted"

    get_response = client.get(f"/categories/{a_category['category_id']}")
    assert get_response.status_code == 404


def test_delete_category_not_found(client):
    response = client.delete("/categories/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Category Not Found"
