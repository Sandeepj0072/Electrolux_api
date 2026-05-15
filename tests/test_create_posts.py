from utils.api_client import APIClient
from utils.file_reader import FileReader


def test_create_post():

    payload = FileReader.read_json(
        "data/post_payload.json"
    )

    response = APIClient.post("/posts", payload)
    print(response.json())

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


