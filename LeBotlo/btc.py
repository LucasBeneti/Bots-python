import requests

value = requests.get("https://blockchain.info/pt/ticker").json()
def brl():
     return str(value['BRL']['15m'])

usd = str(value['USD']['15m'])
