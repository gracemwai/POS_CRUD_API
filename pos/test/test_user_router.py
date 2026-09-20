def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "asmith",
            "password_hash": "hashed_pw",
            "role": "manager",
            "pin_code": "5678",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "asmith"
    assert data["is_active"] is True


def test_list_users(client, a_user):
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_user(client, a_user):
    response = client.get(f"/users/{a_user['user_id']}")
    assert response.status_code == 200
    assert response.json()["username"] == "jdoe"


def test_get_user_not_found(client):
    response = client.get("/users/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User Not Found"


def test_get_user_by_username(client, a_user):
    response = client.get(f"/users/username/{a_user['username']}")
    assert response.status_code == 200
    assert response.json()["user_id"] == a_user["user_id"]


def test_get_user_by_username_not_found(client):
    response = client.get("/users/username/nobody")
    assert response.status_code == 404


def test_update_user(client, a_user):
    response = client.put(f"/users/{a_user['user_id']}", json={"role": "supervisor"})
    assert response.status_code == 200
    assert response.json()["role"] == "supervisor"


def test_update_user_not_found(client):
    response = client.put("/users/99999", json={"role": "supervisor"})
    assert response.status_code == 404


def test_delete_user(client, a_user):
    response = client.delete(f"/users/{a_user['user_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "User deleted"


def test_delete_user_not_found(client):
    response = client.delete("/users/99999")
    assert response.status_code == 404
