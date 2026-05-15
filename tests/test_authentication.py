import requests

def test_with_auth():

    headers = {

        "Authorization": "Bearer fake_token"

    }

    response = requests.get(

        "https://jsonplaceholder.typicode.com/posts",

        headers=headers

    )

    assert response.status_code == 200