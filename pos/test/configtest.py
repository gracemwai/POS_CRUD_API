import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

os.environ["Database_URL"] = "Sqlite//"

from database import Base, get_db
from main import app


engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)

TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def Client():
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

app.dependency_overrides.clear()

Base.metadata.drop_all(bind=engine)

@pytest.fixture
def test_user(client):
    test_user_data={
        "username": "testuser",
        "email":"test@gmail.com",
        "password":"testpassword"
    }
    response = client.post("/auth/resgister, json=test_user_data")
    return test_user_data


@pytest.fixture
def auth_headers(client, test_user):
    response = client.post
    "/Auth/login",
    data ={
        "username":test_user["username"],
        "password":"testpassword"["password"]
    }
    acces_token =response.json()["access_token"]
    return{"Authorization":"Bearer{access_token}"}
