import requests

# test data initialization
rest_api_url = "https://jsonplaceholder.typicode.com/"
path = "posts"
post_id = 1

updated_request_body = {"title": "updated_title", "body": "updated_body", "userId": 1}

headers = {"Content-Type": "application/json; charset=UTF-8"}


def test_post_create_posts():
    response = requests.put(
        f"{rest_api_url}{path}/{post_id}", json=updated_request_body, headers=headers
    )

    posts_data = response.json()

    assert response.status_code == 200
    assert isinstance(posts_data, dict)
    assert "title" in posts_data
    assert posts_data["title"] == updated_request_body["title"]
    assert isinstance(posts_data["title"], str)
    assert "body" in posts_data
    assert posts_data["body"] == updated_request_body["body"]
    assert isinstance(posts_data["body"], str)
    assert "userId" in posts_data
    assert posts_data["userId"] == updated_request_body["userId"]
    assert isinstance(posts_data["userId"], int)
    assert "id" in posts_data
    assert isinstance(posts_data["id"], int)
