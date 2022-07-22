from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health-check")
    assert response.status_code == 200


def test_cat_facts():
    size = 10
    response = client.get(f"/cat-facts/{size}")
    assert response.status_code == 200
    assert len(response.json()) == size
