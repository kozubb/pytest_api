import requests

# test data initialization
rest_api_url = "https://api.zippopotam.us/"
country_code = "us"
zip_code = 28270
not_existed_zip_code = 11111
country = "United States"
state_code = "NC"
state_name = "North Carolina"
city = "Charlotte"

headers = {"Content-Type": "application/json"}


def test_get_zipcode():
    response = requests.get(f"{rest_api_url}{country_code}/{zip_code}", headers=headers)

    zipcode_data = response.json()

    assert response.status_code == 200
    assert isinstance(zipcode_data, dict)
    assert "country" in zipcode_data
    assert zipcode_data["country"] == country
    assert isinstance(zipcode_data["country"], str)
    assert "places" in zipcode_data
    assert isinstance(zipcode_data["places"], list)
    assert zipcode_data["places"][0]["state abbreviation"] == state_code
    assert zipcode_data["places"][0]["state"] == state_name
    assert isinstance(zipcode_data["post code"], str)


def test_get_zipcode_not_found():
    response = requests.get(
        f"{rest_api_url}{country_code}/{not_existed_zip_code}", headers=headers
    )

    assert response.status_code == 404
