from unittest.mock import patch
from src.services.exchange_service import get_usd_to_brl

@patch("src.services.exchange_service.requests.get")
def test_get_usd_to_brl(mock_get):
    mock_get.return_value.json.return_value = {
        "USDBRL": {
            "bid": "5.25"
        }
    }

    result = get_usd_to_brl()

    assert result["usd"] == "5.25"

@patch("src.services.exchange_service.requests.get", side_effect=Exception("API error"))
def test_get_usd_to_brl_error(mock_get):
    result = get_usd_to_brl()

    assert result["usd"] is None
    assert "error" in result