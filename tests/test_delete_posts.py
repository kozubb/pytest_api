import requests

# test data initialization
rest_api_url = "https://jsonplaceholder.typicode.com/"
path = "posts"
post_id = 1


def test_post_create_posts():
    response = requests.delete(f"{rest_api_url}{path}/{post_id}")

    assert response.status_code == 200
