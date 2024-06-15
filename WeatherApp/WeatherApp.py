import tkinter as tk
from tkinter import messagebox
import requests
from geopy.geocoders import Nominatim

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather():
    location = location_entry.get()
    if not location:
        messagebox.showerror("Error", "Please enter a location")
        return

    weather_data = get_weather(api_key, location)
    if weather_data.get('cod') != 200:
        messagebox.showerror("Error", weather_data.get('message'))
    else:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        condition = weather_data['weather'][0]['description']
        
        result_var.set(f"Weather in {city}, {country}:\n"
                       f"Temperature: {temp}°C\n"
                       f"Humidity: {humidity}%\n"
                       f"Condition: {condition}")

def use_gps():
    try:
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode("Your location here")
        location_entry.delete(0, tk.END)
        location_entry.insert(0, location.address)
        display_weather()
    except:
        messagebox.showerror("Error", "Unable to use GPS to detect location")

api_key = "2696fc62b67540cd9bf6646287b8e099"  # Replace with your OpenWeatherMap API key

# Set up the main window
root = tk.Tk()
root.title("Weather App")
root.configure(bg="#e0f7fa")

# Create main frame
main_frame = tk.Frame(root, bg="#e0f7fa", pady=20, padx=20)
main_frame.grid(row=0, column=0, padx=10, pady=10)

# Top frame for input
top_frame = tk.Frame(main_frame, bg="#ffffff", pady=10, padx=10, bd=2, relief=tk.RIDGE)
top_frame.grid(row=0, column=0, padx=10, pady=5)

# Middle frame for buttons
middle_frame = tk.Frame(main_frame, bg="#ffffff", pady=10, padx=10, bd=2, relief=tk.RIDGE)
middle_frame.grid(row=1, column=0, padx=10, pady=5)

# Bottom frame for results
bottom_frame = tk.Frame(main_frame, bg="#ffffff", pady=10, padx=10, bd=2, relief=tk.RIDGE)
bottom_frame.grid(row=2, column=0, padx=10, pady=5)

# Top frame widgets
tk.Label(top_frame, text="Enter Location:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
location_entry = tk.Entry(top_frame, width=30)
location_entry.grid(row=0, column=1, padx=5, pady=5)

# Middle frame widgets
tk.Button(middle_frame, text="Get Weather", command=display_weather, bg="#00796b", fg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
tk.Button(middle_frame, text="Use GPS", command=use_gps, bg="#00796b", fg="#ffffff").grid(row=0, column=1, padx=5, pady=5)

# Bottom frame widgets
result_var = tk.StringVar()
result_label = tk.Label(bottom_frame, textvariable=result_var, bg="#ffffff", justify="left")
result_label.grid(row=0, column=0, padx=5, pady=5)

# Center the main frame in the window
root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Start the Tkinter event loop
root.mainloop()
