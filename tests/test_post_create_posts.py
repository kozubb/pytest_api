import requests

# test data initialization
rest_api_url = "https://jsonplaceholder.typicode.com/"
path = "posts"

request_body = {
    "title": "test_title",
    "body": "body_title",
    "userId": 1
}

headers = {"Content-Type": "application/json; charset=UTF-8"}


def test_post_create_posts():
    response = requests.post(f"{rest_api_url}{path}", json=request_body, headers=headers)

    posts_data = response.json()

    assert response.status_code == 201
    assert isinstance(posts_data, dict)
    assert "title" in posts_data
    assert posts_data["title"] == request_body["title"]
    assert isinstance(posts_data["title"], str)
    assert "body" in posts_data
    assert posts_data["body"] == request_body["body"]
    assert isinstance(posts_data["body"], str)
    assert "userId" in posts_data
    assert posts_data["userId"] == request_body["userId"]
    assert isinstance(posts_data["userId"], int)
    assert "id" in posts_data
    assert isinstance(posts_data["id"], int)

