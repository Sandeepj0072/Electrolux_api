from utils.api_client import APIClient


def test_get_all_posts():

    response = APIClient.get("/posts")

    assert response.status_code == 200

    data = response.json()
    print(data)
    assert len(data) > 0

    assert "userId" in data[0]
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]