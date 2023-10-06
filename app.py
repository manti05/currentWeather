import config
import requests
import tkinter as tk

# Create a variable for you api key inside the config file or here


def get_input():
	# City and Weather Data
	print()
	city_input = input("Enter city: ")
	print("=========================================================================================================")

	location_data = requests.get(
		f"http://api.openweathermap.org/geo/1.0/direct?q={city_input}&limit=5&appid={config.api_key}"
	)
	# Country
	countries = []
	# Iterating over the list
	for i, val in enumerate(location_data.json()):
		# Adding a country to a list
		if val['country']:
			countries.append(val['country'])
			# Statement breaks when the list item doesn't have a state
			# Adding the name of the state if the city is in the US
			# if :
			# 	countries[i] = val['state'] + ", " + val['country']

	# Removing duplicating countries until I find a solution for selecting states
	dup_free_countries = list(set(countries))

	# If there are multiple countries with the same city
	if len(dup_free_countries) > 1:
		# Listing all countries with the same city name
		for country in dup_free_countries:
			print(country)
		# Selecting the country
		country_input = input("Enter country: ")
		# state_input = input("Enter state: ")
		weather_data = requests.get(
			f"https://api.openweathermap.org/data/2.5/weather?q={city_input},{country_input}&units=metric&appid={config.api_key}"
		)
		# using get_weather function
		get_weather(city_input, weather_data)

	else:
		weather_data = requests.get(
			f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=metric&appid={config.api_key}"
		)
		# using get_weather function
		get_weather(city_input, weather_data)


def get_weather(city_input, weather_data):
	# Checking if a valid city name was input
	if weather_data.json()['cod'] == '404':
		print("Invalid city")
	else:
		# Country
		country = weather_data.json()['sys']['country']

		# Weather
		weather = weather_data.json()['weather'][0]['main']
		description = weather_data.json()['weather'][0]['description']

		# Temperatures in °C
		temp = round(weather_data.json()['main']['temp'])
		feel = round(weather_data.json()['main']['feels_like'])
		# temp_min = round(weather_data.json()['main']['temp_min'])
		# temp_max = round(weather_data.json()['main']['temp_max'])

		# Wind in m/s
		wind = weather_data.json()['wind']['speed']

		# Humidity %
		humidity = weather_data.json()['main']['humidity']

		print(f"{city_input}, {country}")
		print()
		print(f"The current weather in {city_input} is: {weather} - {description}")
		print(f"The temperature is: {temp}°C feels like: {feel}°C")
		# print(f"The minimum: {temp_min}°C and maximum: {temp_max}°C today ")
		print(f"The humidity is: {humidity}%")
		print(f"The wind speed is: {wind} m/s")
		print()


if __name__ == '__main__':
	get_input()
