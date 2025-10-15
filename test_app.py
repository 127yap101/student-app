import app

def test_index_route():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Information" in response.data
