from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Task Manager API"}

def test_get_task_status():
    response = client.post(
        "/tasks",
         json = {
        "title": "Complete CI/CD Midterm",
        "completed": False
    })

    task_id = response.json()["id"]

    response = client.get(f"/tasks/{task_id}/status")

    assert response.status_code == 200
    assert response.json() == {
        "task_id": task_id,
        "completed": False
    }


def test_get_task_status_not_found():
    response = client.get("/tasks/999/status")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Task not found"
    }