from fastapi.testclient import TestClient
from app import app, APP_ENV

client = TestClient(app)

def test_liveness_check():
    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "alive"}


def test_readiness_check():
    response = client.get("/health/ready")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ready", 
        "environment": APP_ENV
    }
