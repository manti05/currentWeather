# Import necessary modules
import requests
import config


# Function to fetch location data for a given city
def get_location_data(city):
	try:
		# Send an API request to get location data based on the city
		location_data = requests.get(
			f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={config.api_key}")
		location_data.raise_for_status()
		return location_data.json()  # Return the JSON data received
	except requests.exceptions.RequestException as e:
		print(f"Error fetching location data: {e}")
		return None


# Function to prompt the user to select a country code when multiple countries have the same city name
def get_country_code(city, countries):
	print("Multiple countries with the same city name. Please select a country by its country code:")
	for i, country in enumerate(countries, start=1):
		print(f"{i}. {country['country']} ({country['name']})")

	while True:
		try:
			choice = int(input("Enter the number corresponding to your choice: "))
			if 1 <= choice <= len(countries):
				return countries[choice - 1]['country']  # Return the selected country code
			else:
				print("Invalid choice. Please select a valid number.")
		except ValueError:
			print("Invalid input. Please enter a number.")


# Function to fetch weather data for a city and country (if specified)
def get_weather_data(city, country=None):
	base_url = "https://api.openweathermap.org/data/2.5/weather"
	params = {"q": city, "units": "metric", "appid": config.api_key}
	if country:
		params["q"] = f"{city},{country}"
	try:
		# Send an API request to get weather data for the city and country (if specified)
		weather_data = requests.get(base_url, params=params)
		weather_data.raise_for_status()
		return weather_data.json()  # Return the JSON data received
	except requests.exceptions.RequestException as e:
		print(f"Error fetching weather data: {e}")
		return None


# Function to display weather information for a city
def display_weather(city, country, weather_data):
	# print("Received weather data:")
	# print(weather_data)
	if 'cod' in weather_data and weather_data['cod'] == 404:
		# Check if the API request is valid; if not, display an error message
		print("Invalid city")
	else:
		# Extract and display weather information
		# Weather
		weather = weather_data['weather'][0]['main']
		description = weather_data['weather'][0]['description']

		# Temperatures in °C
		temp = round(weather_data['main']['temp'])
		feel = round(weather_data['main']['feels_like'])

		# Wind in m/s
		wind = weather_data['wind']['speed']

		# Humidity %
		humidity = weather_data['main']['humidity']
		print("Finished assigning variables")

		print(f"{city}, {country}")
		print()
		print(f"The current weather in {city} is: {weather} - {description}")
		print(f"The temperature is: {temp}°C feels like: {feel}°C")
		print(f"The humidity is: {humidity}%")
		print(f"The wind speed is: {wind} m/s")
		print()


# Main function to coordinate the program
def main():
	city = input("Enter city: ")
	location_data = get_location_data(city)
	selected_country_code = None  # Initialize to None

	if location_data:
		countries = [val for val in location_data if val["country"]]
		if len(countries) > 1:
			print("Multiple countries with the same city name. Please specify the country.")
			selected_country_code = get_country_code(city, countries)
			print(f"Selected country code: {selected_country_code}")

		weather_data = get_weather_data(city, selected_country_code)

		if weather_data:
			display_weather(city, selected_country_code, weather_data)
		else:
			print("Failed to fetch weather data.")
	else:
		print("Failed to fetch location data.")


# Entry point of the program
if __name__ == '__main__':
	main()
