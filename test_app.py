from app import app

def test_home():
    tester = app.test_client()  # instantiate test client
    response = tester.get('/')  # make GET request

    assert response.status_code == 200
    assert response.data == b'Hello world!'
