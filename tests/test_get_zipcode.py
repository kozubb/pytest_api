import requests

# Test data initialization
restApiUrl = "https://api.zippopotam.us/"
countryCode = "us"
zipCode = 28270
notExistedZipCode = 11111
country = "United States"
stateCode = "NC"
stateName = "North Carolina"
city = "Charlotte"

headers = {"Content-Type": "application/json"}


def test_get_zipcode():
    response = requests.get(f"{restApiUrl}{countryCode}/{zipCode}", headers=headers)

    response.raise_for_status()

    zipcode_data = response.json()

    assert response.status_code == 200
    assert "country" in zipcode_data
    assert zipcode_data["country"] == country
    assert zipcode_data["places"][0]["state abbreviation"] == stateCode
    assert zipcode_data["places"][0]["state"] == stateName


def test_get_zipcode_not_found():
    response = requests.get(
        f"{restApiUrl}{countryCode}/{notExistedZipCode}", headers=headers
    )

    assert response.status_code == 404
