import requests

user = input("Give username(case sensitive):   ")
link = "https://api.github.com/users/" + user

try:
    print(link)
    response = requests.get(link, timeout=5)
    data = response.json()

    print("\nNAME:  ", data["name"])
    print("BIO:  ", data["bio"])
    print("PUBLIC REPOS:   ", data["public_repos"])
    print("FOLLOWERS:   ", data["followers"])
    print("FOLLOWING:   ", data["following"])

except requests.exceptions.Timeout:
    print("Request took too long")

except requests.exceptions.ConnectionError:
    print("No internet connection")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except Exception as error:
    print("Unexpected error:", error)
