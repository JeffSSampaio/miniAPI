# src/services/exchange_service.py
import requests

def get_usd_to_brl():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  
        data = response.json()
        bid = data.get("USDBRL", {}).get("bid")
        return {"usd": bid}
    except Exception as e:
        return {"usd": None, "error": str(e)}