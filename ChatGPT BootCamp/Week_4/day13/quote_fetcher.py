import requests


response = requests.get("https://api.quotable.io/random")

data = response.json()

print("Quote:")
print(data["content"])
print("- " + data["author"])
