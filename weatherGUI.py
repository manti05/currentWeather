import tkinter as tk
import requests
import config


# Function to get weather data based on latitude and longitude
def get_weather(lat, lon):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lon, "units": "metric", "appid": config.api_key}

    try:
        weather_data = requests.get(base_url, params=params)
        weather_data.raise_for_status()
        return weather_data.json()
    except requests.exceptions.RequestException as e:
        return None


# Function to fetch location data based on a city name
def get_location_data(city):
    try:
        location_data = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={config.api_key}")
        location_data.raise_for_status()
        location_data = location_data.json()
        # Add latitude and longitude to the location data
        for loc in location_data:
            loc["lat"] = loc["lat"]
            loc["lon"] = loc["lon"]
        return location_data
    except requests.exceptions.RequestException as e:
        return None


# Function to fetch and map states to countries
def get_states_and_countries(location_data):
    state_country_map = {}
    for location in location_data:
        if "country" in location:
            country = location["country"]
            state = location.get("state")
            if state:
                state_country_map[state] = country
    return state_country_map


# Function to update the country list based on the entered city
def update_country_list(city):
    location_data = get_location_data(city)
    country_listbox.delete(0, tk.END)

    if location_data:
        state_country_map = get_states_and_countries(location_data)
        for location in location_data:
            if "country" in location:
                country = location["country"]
                state = location.get("state")
                if state:
                    # If state information is available, show "Country - State"
                    country_listbox.insert(tk.END, f"{country} - {state}")
                else:
                    # If no state information is available, show "Country"
                    country_listbox.insert(tk.END, country)


# Function to handle country selection from the listbox
def on_country_select(event):
    index = country_listbox.curselection()
    if index:
        selected_text = country_listbox.get(index)
        if selected_text == "Go back to the list":
            return
        else:
            has_selected_country.set(True)  # Set the flag
            selected_country.set(selected_text)  # Select the country
            location_data = get_location_data(city_entry.get())
            found_location = False
            for location in location_data:
                if "-" in selected_text:
                    country, state = selected_text.split(" - ")
                else:
                    country = selected_text
                    state = None
                if location["country"] == country and location.get("state") == state:
                    found_location = True
                    lat, lon = location["lat"], location["lon"]
                    update_weather_label(lat, lon)
                    break
            if not found_location:
                country_label.config(text="Invalid city")
                selected_country.set("")  # Clear the selected country if the city is invalid


# Function to get the state code (if available) based on city, state, and country
def get_state_code(city, state, country):
    location_data = get_location_data(city)

    if location_data:
        for location in location_data:
            if location["country"] == country:
                if "state_code" in location:
                    return location["state_code"]

    return None  # Return None if state_code is not found


# Function to update the weather information label based on latitude and longitude
def update_weather_label(lat, lon):
    city = city_entry.get()
    country = selected_country.get()

    if not lat or not lon:
        weather_label.config(text="Please select a location")
    else:
        weather_data = get_weather(lat, lon)
        if weather_data:
            weather_label.config(
                text=(
                    f"{city} : {weather_data['weather'][0]['main']} - {weather_data['weather'][0]['description']}\n"
                    f"Temperature: {round(weather_data['main']['temp'])}°C, Feel: {round(weather_data['main']['feels_like'])}°C\n"
                    f"Humidity: {weather_data['main']['humidity']}%\n"
                    f"Wind Speed: {weather_data['wind']['speed']} m/s"
                )
            )
        else:
            weather_label.config(text="Failed to fetch weather data")


# Function to go back to the country list after selecting a country
def go_back_to_list():
    go_back_button.pack_forget()  # Remove the "Go Back" button
    country_listbox.pack()  # Add the listbox back
    update_country_list(city_entry.get())  # Re-populate the listbox


# Function to replace the listbox with a button
def replace_listbox_with_button():
    country_listbox.pack_forget()  # Remove the listbox
    go_back_button.pack()  # Add the "Go Back" button


# Create the main window
window = tk.Tk()
window.title("Weather App")

# Set the window size to a fixed value
window.geometry("300x400")  # Adjust these dimensions as needed

# Create a label for city input
city_label = tk.Label(window, text="Enter city:")
city_label.pack()

# Create an entry field for city input
city_entry = tk.Entry(window, justify='center')
city_entry.pack()

# Create a label to display the country
country_label = tk.Label(window, text="")
country_label.pack()

# Create a listbox to display countries
country_listbox = tk.Listbox(window)
country_listbox.pack()

# Bind the listbox to the selection function
country_listbox.bind("<<ListboxSelect>>", on_country_select)

# Create a label to display weather information
weather_label = tk.Label(window, text="")
weather_label.pack()

# Create a variable to store the selected country
selected_country = tk.StringVar()
country_listbox.config(listvariable=selected_country)

# Create a flag to track if a country is selected
has_selected_country = tk.BooleanVar()
has_selected_country.set(False)

# Create a button to go back to the country list
go_back_button = tk.Button(window, text="Go Back", command=go_back_to_list)
go_back_button.pack_forget()  # Initially, the button is hidden

# Bind events to update the country list
city_entry.bind("<KeyRelease>", lambda event=None: update_country_list(city_entry.get()))
city_entry.bind("<FocusIn>", lambda event=None: update_country_list(city_entry.get()))

# Start the GUI main loop
window.mainloop()
