from utils.api_client import APIClient
from jsonschema import validate

post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}


def test_post_schema():

    response = APIClient.get("/posts/1")

    data = response.json()
    print(data)
    validate(instance=data, schema=post_schema)


def test_get_user_full_validation():

    response = APIClient.get("/users/1")

    assert response.status_code == 200


    data = response.json()
    print(data)

    assert data["id"] == 1

    assert "name" in data

    assert "email" in data
