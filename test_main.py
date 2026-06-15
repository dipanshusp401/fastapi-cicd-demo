from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    # assert response.json() == {"message": "Hello from Docker!"}
    assert response.json() == {"message": "Wrong message!"}
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()
