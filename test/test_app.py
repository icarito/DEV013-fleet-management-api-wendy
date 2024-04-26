"""endpoints unit tests"""
def test_get_taxis(client):
    """Testing /taxis route is available"""
    response = client.get('/taxis')
    assert response.status_code == 200

def test_get_taxis_pagination(client):
    """Testing /taxis pagination is correctly working"""
    response = client.get('/taxis?page=2&per_page=10')
    data = response.get_json()
    assert len(data) == 10  # Checks if returns 10 taxis per page