import os

# Must be set BEFORE `database` (and anything importing it) is loaded,
# since database.py reads this env var at import time and raises if
# it's missing. Using a file-backed SQLite DB (not :memory:) so every
# connection opened during a test sees the same schema/data — plain
# ":memory:" gives each new connection its own empty database, which
# breaks FastAPI's per-request session pattern.
os.environ["database_url"] = "sqlite:///./test.db"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, get_db
from main import app

engine = create_engine(
    "sqlite:///./test.db", connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def _fresh_database():
    # Runs before AND after every test: build a clean schema, hand
    # control to the test, then tear it down. The original version of
    # this fixture ran create_all/drop_all once at import time instead
    # of per-test, and never yielded, so tests were sharing (and
    # eventually running against a dropped) schema.
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def a_category(client):
    response = client.post(
        "/categories/", json={"name": "Beverages", "description": "Drinks"}
    )
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def a_user(client):
    payload = {
        "username": "jdoe",
        "password_hash": "hashed_pw",
        "role": "cashier",
        "pin_code": "1234",
    }
    response = client.post("/users/", json=payload)
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def a_customer(client):
    response = client.post(
        "/customers/", json={"first_name": "Jane", "last_name": "Roe"}
    )
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def a_supplier(client):
    response = client.post(
        "/suppliers/",
        json={"company_name": "Acme Supplies", "email": "acme@example.com"},
    )
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def a_product(client, a_category):
    response = client.post(
        "/products/",
        json={
            "barcode": "0001112223334",
            "name": "Cola 500ml",
            "category_id": a_category["category_id"],
            "price": "1.50",
        },
    )
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def a_sale(client, a_user, a_customer):
    response = client.post(
        "/sales/",
        json={
            "customer_id": a_customer["customer_id"],
            "user_id": a_user["user_id"],
            "subtotal": "10.00",
            "tax_amount": "1.00",
            "discount_amount": "0.00",
            "grand_total": "11.00",
            "status": "completed",
        },
    )
    assert response.status_code == 200
    return response.json()

