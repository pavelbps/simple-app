import pytest
from app.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    res = client.get("/")
    assert res.status_code == 200

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200

def test_get_users(client):
    res = client.get("/api/users")
    assert res.status_code == 200

def test_create_user_success(client):
    res = client.post("/api/users", json={
        "name": "test",
        "email": "test@test.com"
    })
    assert res.status_code == 201

def test_create_user_fail(client):
    res = client.post("/api/users", json={})
    assert res.status_code == 400
