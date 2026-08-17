import requests

response = requests.get("http://api.weatherapi.com/v1/current.json?key=dec73d793a174cf299721156262206&q=Kolkata")

data = response.json()

try:
    response = requests.get("http://api.weatherapi.com/v1/current.json?key=dec73d793a174cf299721156262206&q=Kolkata")
    response.raise_for_status()
    data = response.json()

    # Checks if the server returned an error (404, 500, etc.)


    data = response.json()

    print("\n📜 Weather Report")
    print("\nPlace: ", data["location"]["name"])
    print("Time: ", data["location"]["localtime"])
    print("\nTemperatur(Celsius): ", data["current"]["temp_c"])
    print("Wind Speed: ", data["current"]["wind_kph"], "kmph")
    print("Humidity: ", data["current"]["humidity"])
    print("Feels like: ", data["current"]["feelslike_c"], "degrees Celsius")

except requests.exceptions.ConnectionError:
    print("❌ No internet connection. Please check your network and try again.")

except requests.exceptions.Timeout:
    print("⏳ The server is taking too long to respond. Try again later.")

except requests.exceptions.HTTPError:
    print("⚠️ The quote server is currently unavailable.")

except requests.exceptions.RequestException as e:
    print(f"🚨 Something went wrong: {e}")
