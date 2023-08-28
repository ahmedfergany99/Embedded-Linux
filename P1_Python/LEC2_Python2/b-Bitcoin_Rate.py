import requests

#get from API
LINK = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

#Print Bitcoin rate automatically
print(LINK.json()['bpi']['USD'])