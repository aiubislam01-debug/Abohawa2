from tkinter import *
from datetime import datetime
import requests
import pytz
import os

def get_hourly_data(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,weathercode&timezone=auto"
    r = requests.get(url)
    data = r.json()

    times = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]
    codes = data["hourly"]["weathercode"]
    my_timezoone = data['timezone']

    current_time = datetime.now(pytz.timezone(my_timezone))
    index = 0
    for i, t in enumerate(times):
        dt = datetime.fromisoformat(t)
        if dt.hour == now.hour and dt.day == now.day:
            index = i
            break

    hourly = []
    for i in range(index, index + 24):
        if i >= len(times):
            break
        temp = round(temps[i], 1)
        dt = datetime.fromisoformat(times[i])
        time_str = dt.strftime("%I %p")
        condition = weather_code_to_text(codes[i])
        hourly.append((time_str, temp, condition, codes[i]))

    return hourly


def weather_code_to_text(code):
    mapping = {
        0: "Clear",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Rime Fog",
        51: "Light Drizzle",
        53: "Drizzle", 55: "Heavy Drizzle",
        61: "Light Rain",
        63: "Rain",
        65: "Heavy Rain",
        71: "Light Snow",
        73: "Snow",
        75: "Heavy Snow",
        80: "Showers",
        95: "Thunderstorm"
    }


def show_hourly_forecast(root, hourly_data, x=0, y=0, width=900, height=150):

    if hasattr(root, "forecast_outer"):
        root.forecast_outer.destroy()

    outer_forecast = Frame(root, bg=root.cget("bg"))
    outer_forecast.place(x=x, y=y, width=width, height=height)
    root.forecast_outer = outer_forecast

    forecast_canvas = Canvas(outer_forecast, bg=root.cget("bg"), highlightthickness=0)
    scroll_x = Scrollbar(outer_forecast, orient=HORIZONTAL, command=forecast_canvas.xview)
    forecast_canvas.configure(xscrollcommand=scroll_x.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    forecast_canvas.pack(fill="both", expand=True)

    inner_forecast = Frame(forecast_canvas, bg=root.cget("bg"))
    forecast_canvas.create_window((0, 0), window=inner_forecast, anchor="nw")

    def update_scroll(event):
        forecast_canvas.configure(scrollregion=forecast_canvas.bbox("all"))
    inner_forecast.bind("<Configure>", update_scroll)

    for time_str, temp, cond, code in hourly_data:
        block = Frame(inner_forecast, bg="#f8f8f8", width=100, height=120,
                      highlightbackground="#ccc", highlightthickness=1)
        block.pack(side=LEFT, padx=5, pady=10)

        Label(block, text=time_str, fg="#333", bg="#f8f8f8",
              font=("Segoe UI", 9, "bold")).pack(pady=(5,0))


        Label(block, text=f"{temp}°C", fg="#0078d7", bg="#f8f8f8",
              font=("Segoe UI", 11, "bold")).pack()
        Label(block, text=cond, fg="#555", bg="#f8f8f8",
              font=("Segoe UI", 9)).pack(pady=(0, 5))



root = Tk()
root.title("Next 24 Hours Forecast")
root.geometry("950x250")
root.config(bg="white")


lat, lon = 23.8103, 90.4125
hourly_data = get_hourly_data(lat, lon)
show_hourly_forecast(root, hourly_data, x=20, y=20, width=900, height=150)

root.mainloop()

