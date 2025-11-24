from unittest.mock import patch
from src.app import create_app

def test_usd_to_brl_route_success(client):
    with patch("src.routes.get_usd_to_brl") as mock_api:
        mock_api.return_value = {"usd": "5.00"}

        response = client.get("/exchange/usd-to-brl")
        data = response.get_json()

        assert response.status_code == 200
        assert data["usd"] == "5.00"

def test_usd_to_brl_route_fail(client):
    with patch("src.routes.get_usd_to_brl") as mock_api:
        mock_api.return_value = {"usd": None, "error": "API offline"}

        response = client.get("/exchange/usd-to-brl")
        assert response.status_code == 503
