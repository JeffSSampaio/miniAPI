# src/services/exchange_service.py
import requests

def get_usd_to_brl():
    """
    Chama a API externa e retorna a cotação (bid) do USD para BRL.
    Retorna dicionário com a chave "usd" (pode ser None em caso de erro).
    """
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    response = requests.get(url)
    data = response.json()

    # pega com segurança: evita KeyError se estrutura mudar
    bid = data.get("USDBRL", {}).get("bid")
    return {"usd": bid}
