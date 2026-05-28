import requests

# Your API key
api_key = "5f54f23ba118ee68b9aa63f184a953ea"

# Ask user for city
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Get weather data
response = requests.get(url)

# Convert to JSON
data = response.json()


# Check if city exists
if data["cod"] == 200:

    temperature = data["main"]["temp"]

    humidity = data["main"]["humidity"]

    condition = data["weather"][0]["description"]

    print("\nWeather in", city)

    print("Temperature:", temperature,"°C")

    print("Humidity:", humidity,"%")

    print("Condition:", condition)

else:

    print("City not found!")