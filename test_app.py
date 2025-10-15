import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Information" in response.data

def test_add_and_delete(client):
    # Add student
    response = client.post("/add", data={"name": "Test", "email": "test@example.com", "course": "TestCourse"})
    assert response.status_code == 302  # Redirect after add

    # Delete student
    students = client.get("/").data.decode()
    last_id = students.count("Delete")  # simple way to guess last student id
    response = client.get(f"/delete/{last_id}")
    assert response.status_code == 302
