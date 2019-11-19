from lbcapi3 import api
import asyncio

hmac_key = 	'e5faa55f0bc9db8225593602eb0649db'
hmac_secret = '291d880f1458af58df01220e600416c5a8681b8c08e935306b801ccb20e5419e'

conn = api.hmac(hmac_key, hmac_secret)

precio_dolarJson = conn.call('GET', '/api/equation/USD_in_DOLARTODAY').json()
btc_in_bsJson = conn.call('GET', '/api/equation/btc_in_usd*USD_in_DOLARTODAY').json()
btc_in_usdJson = conn.call('GET', '/api/equation/btc_in_usd').json()

"""
async def BtcInUsd():
	btc_in_usd = btc_in_usdJson['data']
	await print(btc_in_usd)

loop = asyncio.get_event_loop()
loop.run_until_complete(BtcInUsd())
loop.close()
"""

btc_in_usd = btc_in_usdJson['data']
precio_dolar = precio_dolarJson['data']
btc_in_bs = btc_in_bsJson['data']


print(round(float(precio_dolar)))