from utils.api_client import APIClient


def test_invalid_post():

    response = APIClient.get("/posts/99999")

    assert response.status_code == 404 or response.json() == {}


from utils.api_client import APIClient


def test_invalid_endpoint():

    response = APIClient.get("/invalidendpoint")

    assert response.status_code == 404

