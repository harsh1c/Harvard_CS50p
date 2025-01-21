import pytest
from unittest.mock import patch
from project import get_location_details, wikidata_code_extractor, ask_info



def test_ask_info_yes_valid_choice():
    # Simulating "yes" for the first input and "city" for the second input
    with patch("builtins.input", side_effect=["yes", "city"]):
        result = ask_info()
        assert result == "city"  # Expecting "city" as the final return

# Test for get_location_details
def test_get_location_details_success(mocker):
    # Mock successful API response
    mock_response = {
        "features": [
            {"properties": {"name": "India", "result_type": "country"}},
            {"properties": {"name": "New York", "result_type": "city"}},
        ]
    }

    # Mock requests.get to return the mock response
    mocked_get = mocker.patch("requests.get")
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = mock_response

    # Test with place_type "no" (no filtering)
    result = get_location_details("India", "no", "fake_api_key")
    assert len(result) == 2  # Both India and New York should be returned

    # Test with place_type "country" (should only return "India")
    result = get_location_details("India", "country", "fake_api_key")
    assert len(result) == 1
    assert result[0]["name"] == "India"

# Test for wikidata_code_extractor
def test_wikidata_code_extractor(mocker):
    # Mock successful API response with valid Wikidata code
    mock_response = {
        "features": [
            {"properties": {"wiki_and_media": {"wikidata": "Q12345"}}}
        ]
    }
    mocked_get = mocker.patch("requests.get")
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = mock_response

    result = wikidata_code_extractor("test_place_id", "fake_api_key")
    assert result == "Q12345"  # Expecting the extracted Wikidata code





