# Read data from an API call that gives structured data in JSON format and arrange that data in the requested format.


import requests
from requests import request

url = 'http://10.4.25.3:3000/qa-videos-api/v1/checkTokens/FYPoirG9N7niwT8v9/y2Xosxv6FDZCihAKt'

print(requests.get(url).json())

url = "https://www.alphavantage.co/query"
headers = {"CUSTOM_TOKEN_HEADER": "CUSTOM_TOKEN"}
querystring = {"function": "CURRENCY_EXCHANGE_RATE", "from_currency": "BTC", "to_currency": "USD",
               "apikey": "alpha_vantage_api_key"}
response = request("GET", url, headers=headers, params=querystring).json()
