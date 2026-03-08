import requests

# test data initialization
base_url = "https://quickpizza.grafana.com"

login_request_body = {"username": "default", "password": "12345678"}


def test_login_quick_pizza():
    csrf_response = requests.post(f"{base_url}/api/csrf-token")

    csrf_token = csrf_response.cookies["csrf_token"]

    assert csrf_response.status_code == 200
    assert "csrf_token" in csrf_response.cookies

    login_response = requests.post(
        f"{base_url}/api/users/token/login?set_cookie=true",
        json=login_request_body,
        headers={"Content-Type": "application/json", "X-Csrf-Token": csrf_token},
    )

    assert login_response.status_code == 200
    assert "token" in login_response.json()
    user_token = login_response.json()["token"]

    ratings_response = requests.get(
        f"{base_url}/api/ratings", cookies={"qp_user_token": user_token}
    )
    ratings_data = ratings_response.json()

    assert ratings_response.status_code == 200
    assert "ratings" in ratings_data
    for item in ratings_data["ratings"]:
        assert "pizza_id" in item
