# Weather Application

This README provides an overview of two weather applications. One is a command-line application (app.py) that provides weather information for a given city, while the other is a graphical user interface (GUI) application (weatherGUI.py) that offers a more interactive experience.

## Table of Contents
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Command-Line Weather Application (app.py)](#command-line-weather-application-apppy)
- [Graphical User Interface Weather Application (weatherGUI.py)](#graphical-user-interface-weather-application-weatherguipy)
- [Author](#author)

## Requirements

Before using these weather applications, ensure you meet the following requirements:

- **Python**: These applications require Python 3.x to run. If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads).

- **OpenWeatherMap API Key**: To fetch weather data, you need to create an account and obtain an API key from [OpenWeatherMap](https://openweathermap.org/). You will need to place this API key in a `config.py` file, as explained in the "Configuration" section below.

No additional packages or libraries need to be installed, as the necessary dependencies (`requests` and `tkinter`) are part of Python's standard library.

## Configuration

Before running either application, follow these steps to configure your OpenWeatherMap API key:

1. Create an account on [OpenWeatherMap](https://openweathermap.org/) if you haven't already.

2. Obtain an API key from your OpenWeatherMap account.

3. Create a `config.py` file in the same directory as the application files.

4. In the `config.py` file, format it as follows, replacing `"YOUR_API_KEY_HERE"` with your actual OpenWeatherMap API key:

```python
api_key = "YOUR_API_KEY_HERE"
```
By completing these steps, you'll be ready to use these applications to fetch location and weather data, making it easy to access up-to-date weather information for various locations around the world.

Enjoy using these weather applications and stay informed about the weather conditions in your desired locations!

## Command-Line Weather Application (app.py)

### Features
- Fetches location data for a given city using the OpenWeatherMap API.
- Allows the user to select a country code when multiple countries have the same city name.
- Fetches weather data based on the city and country (if specified).
- Displays weather information, including weather conditions, temperature, humidity, and wind speed.

### Usage
1. Run `app.py` in your command-line interface.
2. Enter the name of the city for which you want weather information.
3. The application will prompt you to select a country code if multiple countries share the same city name.
4. It will then fetch and display the weather information for the provided city.

## Graphical User Interface Weather Application (weatherGUI.py)

### Features
- Provides a graphical user interface for an interactive experience.
- Allows the user to input a city and view weather information for that location.
- Dynamically updates the list of available countries based on the entered city.
- Displays weather information for the selected city and country.
- Provides a "Go Back" option to return to the list of available countries.

### Usage
1. Run `weatherGUI.py` to start the graphical weather application.
2. Enter the name of the city in the input field.
3. The application will dynamically update the list of countries as you type the city name.
4. Select a country from the list to view weather information for that location.
5. To go back to the list of available countries, click the "Go Back" button.

### Issue with GUI Version
In the graphical user interface (GUI) version of the Weather Application (weatherGUI.py), a specific issue exists.
The list isn't displayed again until the "Go Back" button is clicked, this poses a problem of not showing the updating list when inputting a different city.

Before inputting a new city, please click the "Go Back" button to see the updated list of countries.

## Author
Mantas Stankevicius

For questions or assistance, please contact mantas@mantascodes.com.
