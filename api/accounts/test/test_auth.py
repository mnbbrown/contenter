import pytest
from api.accounts.service import create_user


def test_client_credentials_token(db, client):
    create_user(db, "test@test.com", "password")
    db.commit()
    response = client.post("/auth/token", data={"username": "test@test.com", "password": "password"})
    assert response.status_code == 200
    assert response.json().get("access_token") is not None


def test_invalid_client_credentials_token(db, client):
    response = client.post("/auth/token", data={"username": "bad_test@test.com", "password": "password"})
    assert response.status_code == 401
