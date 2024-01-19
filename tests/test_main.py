from fastapi.testclient import TestClient

from app.main import app
from app.services import play_rps

client = TestClient(app)


def test_read_say_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello What is love"}


def test_rps():
    response = client.get("/rps", params={
        "choice": "Ножницы"
    })
    result = response.json()
    assert response.status_code == 200
    assert "status" in result
    assert "massage" in result
