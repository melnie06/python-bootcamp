import requests

site = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(site)


# print(response)
joke = response.json()
# print(type(joke))
print(joke['setup'])
print(joke['punchline'])
