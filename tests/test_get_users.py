import requests

# test data initialization
rest_api_url = "https://jsonplaceholder.typicode.com/"
path = "users"
not_existed_path = "userstest"
expected_name = "Kurtis Weissnat"
expected_username = "Elwyn.Skiles"
expected_city = "Howemouth"
expected_company_name = "Johns Group"
expected_catch_phrase = "Configurable multimedia task-force"

headers = {"Content-Type": "application/json"}


def test_get_users():
    response = requests.get(f"{rest_api_url}{path}/7", headers=headers)

    users_data = response.json()

    assert response.status_code == 200
    assert isinstance(users_data["id"], int)
    assert "name" in users_data
    assert users_data["name"] == expected_name
    assert isinstance(users_data["name"], str)
    assert users_data["username"] == expected_username
    assert "city" in users_data["address"]
    assert users_data["address"]["city"] == expected_city
    assert users_data["company"]["name"] == expected_company_name
    assert users_data["company"]["catchPhrase"] == expected_catch_phrase
    assert isinstance(users_data["address"], dict)


def test_get_users_not_found():
    response = requests.get(f"{rest_api_url}{not_existed_path}/7", headers=headers)

    assert response.status_code == 404
