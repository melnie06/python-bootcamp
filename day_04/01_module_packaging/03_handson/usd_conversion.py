import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")

# Get the latest conversion rate from USD to PHP


peso_value = response.json()
print(peso_value["rates"]["PHP"])



