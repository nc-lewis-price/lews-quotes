from pydantic.main import BaseModel
import pytest
from fastapi.testclient import TestClient
from src.app import app

@pytest.fixture()
def client():
    return TestClient(app)

def test_healthcheck_200_responds_with_all_good(client):
    res = client.get("/api/healthcheck")
    res_body = res.json()
    assert res.status_code == 200
    assert res_body == {"msg": "all good!"}

def test_random_200_responds_with_a_random_quote(client):
    res = client.get("/api/random")
    res_body = res.json()
    quote = res_body["quote"]

    assert res.status_code == 200
    assert isinstance(quote["author"], str)
    assert isinstance(quote["content"], str)
    assert isinstance(quote["length"], int)

def test_invalid_path_404(client):
    res = client.get("/api/notapath")
    assert res.status_code == 404
