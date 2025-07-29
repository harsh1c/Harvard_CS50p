import requests
import sys

try:
    if len(sys.argv) == 2:
        no_of_coins = float(sys.argv[1])
    else:
        sys.exit("enter only 1 argument")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    code = response.json()

    prices = code["bpi"]
    usd_price = prices["USD"]
    rate_in_usd = usd_price["rate_float"]

    #Price of all the bitcoins in USD
    total = no_of_coins * rate_in_usd
    print(f"${total:,}", end="")

except requests.RequestException:
    print("Request Error")