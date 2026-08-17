import requests

try:
    response = requests.get("https://api.quotable.io/random", timeout=5)

    # Checks if the server returned an error (404, 500, etc.)
    response.raise_for_status()

    data = response.json()

    print("\n📜 Random Quote")
    print(data["content"])
    print("- " + data["author"])

except requests.exceptions.ConnectionError:
    print("❌ No internet connection. Please check your network and try again.")

except requests.exceptions.Timeout:
    print("⏳ The server is taking too long to respond. Try again later.")

except requests.exceptions.HTTPError:
    print("⚠️ The quote server is currently unavailable.")

except requests.exceptions.RequestException as e:
    print(f"🚨 Something went wrong: {e}")
