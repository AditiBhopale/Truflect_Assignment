import app

def test_get_banks():
    client = app.app.test_client()
    response = client.get('/banks')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_branches_valid():
    client = app.app.test_client()
    response = client.get('/branches/Example Bank')
    assert response.status_code == 200

def test_get_branches_invalid():
    client = app.app.test_client()
    response = client.get('/branches/NonExistentBank')
    assert response.status_code == 404
