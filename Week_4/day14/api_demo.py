
import requests


try:
    response = requests.get(
        "https://api.github.com",
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    print("API is working")
    print(data)

except requests.exceptions.Timeout:
    print("Request took too long")

except requests.exceptions.ConnectionError:
    print("No internet connection")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except Exception as error:
    print("Unexpected error:", error)
