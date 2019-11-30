from lbcapi3 import api
import urllib, json
import requests
"""
hmac_key = 	'e5faa55f0bc9db8225593602eb0649db'
hmac_secret = '291d880f1458af58df01220e600416c5a8681b8c08e935306b801ccb20e5419e'

conn = api.hmac(hmac_key, hmac_secret)


def Dolartoday():
	precio_dolarJson = conn.call('GET', '/api/equation/USD_in_DOLARTODAY').json()
	precio_dolar = precio_dolarJson['data']
	return round(float(precio_dolar))


def BtcInVes():
	btc_in_bsJson = conn.call('GET', '/api/equation/btc_in_usd*USD_in_DOLARTODAY').json()
	btc_in_bs = btc_in_bsJson['data']
	return round(float(btc_in_bs))

def BtcInUsd():
	btc_in_usdJson = conn.call('GET', '/api/equation/btc_in_usd').json()
	btc_in_usd = btc_in_usdJson['data']
	return round(float(btc_in_usd))
"""

#cambio el tiempo real


def Dolartoday():
	with urllib.request.urlopen(f"https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=VES&api_key=dc1bab01a536aaec3593f72a057f8494701868e70a3a6ea6005e6a5e4b70b29e") as url:
		data = json.loads(url.read().decode())
		price = data['VES']
		return round(float(price))

def BtcInVes():
	with urllib.request.urlopen(f"https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=VES&api_key=dc1bab01a536aaec3593f72a057f8494701868e70a3a6ea6005e6a5e4b70b29e") as url:
		data = json.loads(url.read().decode())
		price = data['VES']
		return round(float(price))

def BtcInUsd():
	with urllib.request.urlopen(f"https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&api_key=dc1bab01a536aaec3593f72a057f8494701868e70a3a6ea6005e6a5e4b70b29e") as url:
		data = json.loads(url.read().decode())
		price = data['USD']
		return round(float(price))

