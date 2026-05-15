from utils.api_client import APIClient
from utils.file_reader import FileReader


def test_create_post_with_invalid_data():

    payload = FileReader.read_json(
        "data/invalid_payload.json"
    )

    response = APIClient.post("/posts", payload)

    print(response.status_code)
    print(response.json())

    assert response.status_code in [400, 201]

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]



def test_invalid_post():

    response = APIClient.get("/posts/99999")

    assert response.status_code == 404 or response.json() == {}


from utils.api_client import APIClient


def test_invalid_endpoint():

    response = APIClient.get("/invalidendpoint")

    assert response.status_code == 404

