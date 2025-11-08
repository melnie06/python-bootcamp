import requests

site = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(site)

joke = response.json()
print(joke['setup'])
print(joke['punchline'])
