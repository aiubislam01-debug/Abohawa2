from current_location import get_location
from hourly_forecast2 import get_hourly_data, show_hourly_forecast
import requests as req
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import *
from timezonefinder import TimezoneFinder
import pytz
import speech_recognition as sr
import threading
from folium import *
import webview as web
import math
from customtkinter import *
from gtts import gTTS
import os
import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as gemini

def open():
    
    def values(event):
        
        selection = combobox2.get()
        
        if selection == "Integer":
            temp = int(weather_data['main']['temp'])
            t.config(text = f"{temp}°C")
            feelings = int(weather_data['main']['feels_like'])
            feeling_temp.config(text = f"{feelings}°C")
            tempe = int(data['list'][7]['main']['temp'])
            forecast_temp.config(text = f"Temperature\n{tempe}°C")
            tempe2 = int(data['list'][15]['main']['temp'])
            forecast_day2_temp.config(text = f"Temperature\n {tempe2}°C")
            max_tempe = int(weather_data['main']['temp_max'])
            max_temp.config(text = f'{max_tempe}°C')
            
            min_tempe = int(weather_data['main']['temp_min'])
            min_temp.config(text = f'{min_tempe}°C')
        if selection == "Floating":
            temp = weather_data['main']['temp']
            t.config(text = f"{temp}°C")
            feelings = weather_data['main']['feels_like']
            feeling_temp.config(text = f"{feelings}°C")
            tempe = data['list'][7]['main']['temp']
            forecast_temp.config(text = f"Temperture\n{tempe}°C")
            tempe2 = data['list'][15]['main']['temp']
            forecast_day2_temp.config(text = f"Temperature\n {tempe2}°C")
            
            max_tempe = weather_data['main']['temp_max']
            max_temp.config(text = f'{max_tempe}°C')
            
            min_tempe = weather_data['main']['temp_min']
            min_temp.config(text = f'{min_tempe}°C')
            
    def com(event):

        select = combobox.get()
        
        if select == 'Fahrenheit':
            temp = int(weather_data['main']['temp']*(1.8)+32)
            t.config(text = f"{temp}°F")
        
            feelings = int(weather_data['main']['feels_like']*1.8+32)
            feeling_temp.config(text = f"{feelings}°F")
        
            tempe = int(data['list'][7]['main']['temp']*(1.8)+32)
            forecast_temp.config(text = f"Temperature\n{tempe}°F")
            
            tempe2 = int(data['list'][15]['main']['temp']*(1.8)+32)
            forecast_day2_temp.config(text = f"Temperature\n {tempe2}°F")
            
            min_tempe = int(weather_data['main']['temp_min']*(1.8)+32)
            min_temp.config(text = f'{min_tempe}°F')
            
            max_tempe = int(weather_data['main']['temp_max'])
            max_temp.config(text = f"{max_tempe}°F")
        
        if select == 'Kelvin':
            temp = int(weather_data['main']['temp']+273.15)
            t.config(text = f"{temp}°K")
        
        
            feelings = int(weather_data['main']['feels_like']+273.15)
            feeling_temp.config(text = f"{feelings}°K")
        
            tempe = int(data['list'][7]['main']['temp']+273.15)
            forecast_temp.config(text = f"Temperature\n{tempe}°K")
            
            tempe2 = int(data['list'][15]['main']['temp']+273.15)
            forecast_day2_temp.config(text = f"Temperature\n {tempe2}°K")
            
            max_tempe = int(weather_data['main']['temp_max'] + 273.15)
            max_temp.config(text = f"{max_tempe}°K")
            
            min_tempe = int(weather_data['main']['temp_min'] + 273.15)
            min_temp.config(text = f"{max_tempe}°K")
            
        if select == 'Celsius':
            temp = int(weather_data['main']['temp'])
            t.config(text = f"{temp}°C")
        
        
            feelings = int(weather_data['main']['feels_like'])
            feeling_temp.config(text = f"{feelings}°C")
        
            tempe = int(data['list'][7]['main']['temp'])
            forecast_temp.config(text = f"Temperature\n{tempe}°C")
            
            tempe2 = int(data['list'][15]['main']['temp'])
            forecast_day2_temp.config(text = f"Temerature\n {tempe2}°C")
            
            max_tempe = int(weather_data['main']['temp_max'])
            max_temp.config(text = f'{max_tempe}°C')
            
            min_tempe = int(weather_data['main']['temp_min'])
            min_temp.config(text = f'{min_tempe}°C')
            
    def weather(city):
        global condition,data,local_time,lati,long,zone,sunrise,weather_data,city_now
        api = "644be7103a977fa6cc8f498edaff9983"
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api}"         
                
        try:
            req.get(link,timeout = 5)
        
        except req.ConnectionError:
            messagebox.showwarning("",'You are currently offline!')
        
        
        geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=644be7103a977fa6cc8f498edaff9983"
        forecast_link = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=644be7103a977fa6cc8f498edaff9983&units=metric"
        loc = req.get(geo).json()

        
        long = loc[0]['lon']
        lati = loc[0]['lat']
        
        hourly_data = get_hourly_data(lati, long)
        show_hourly_forecast(gui, hourly_data, x = 800, y= 550,width = 400)
        
        data = req.get(forecast_link).json()
    
        weather_data = req.get(link).json()
        wind_deg = weather_data['wind']['deg']
        print(wind_deg)
        air_quality_link = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lati}&lon={long}&appid=644be7103a977fa6cc8f498edaff9983"
        
        air_quality_data = req.get(air_quality_link).json()
    
        if 'rain' in weather_data:
            rain_mm = weather_data['rain'].get('1h',0)
            print(f"hi{rain_mm}")
        if weather_data['cod'] == 200:
            
            
            temp = int(weather_data['main']['temp'])
            city = weather_data['name']
            humidity = weather_data['main']['humidity']
            
            condition = weather_data['weather'][0]['main']
            des = weather_data['weather'][0]['description']
            icon = weather_data['weather'][0]['icon']
            icon2 = PhotoImage(file = f"{icon}@2x.png")
            lbl_sun.config(image = icon2,bg = 'white',height = 50,width = 60)
            lbl_sun.image = icon2
            lbl_sun.place(x = 650,y = 510)
            
            wind_speed = int(weather_data['wind']['speed']*3.6)
            wind_deg = weather_data['wind']['deg']
            current_angle = wind_deg
            update_needle(current_angle)
            
            lbl_crnt.config(text = f'Today in {city}')
            
            pressure = weather_data['main']['pressure']
            feels_like = int(weather_data['main']['feels_like'])
            feeling_temp.config(text = f'{feels_like}°C')
            
            min_tempe = int(weather_data['main']['temp_min'])
            min_temp.config(text = f'{min_tempe}°C')
           
            
            max_tempe = int(weather_data['main']['temp_max'])
            max_temp.config(text = f'{max_tempe}°C')
            
            
            visibility_d = int(weather_data['visibility']/1000)
            visibility.config(text = f"{visibility_d} KM")
            
            
            clouds_wxyz = weather_data['clouds']['all']
            clouds.config(text = f'{clouds_wxyz}%')
            
            
            tz = TimezoneFinder()
            timezone = tz.timezone_at(lng = long,lat = lati)
            zone = pytz.timezone(timezone)
            
            sunrise = weather_data['sys']['sunrise']
            sunrise_time = datetime.fromtimestamp(sunrise,zone)
            st = sunrise_time.strftime("%A")
            srt = sunrise_time.strftime("%I:%M %p")
            sunrise_optional_lbl.config(text = f"Sunrise at {srt}")
            
            sunset = weather_data['sys']['sunset']
            sunset_time = datetime.fromtimestamp(sunset,zone)
            st2 = sunset_time.strftime("%A")
            sst = sunset_time.strftime("%I:%M %p")
            sunset_optional_lbl.config(text = f"Sunset at {sst}")
            
            t.config(text = f"{temp}°C")
            h.config(text = f"{humidity} %")
            
            d.config(text = des)
            d.place(x = 390,y = 568)
            
            w.config(text = f"{wind_speed} km/h")
            
            p.config(text = f"{pressure} hPa")
            btn_bng.config(text = "shunoon", command=lambda :speak_weather_bangla(city,condition, temp, feels_like,humidity, wind_speed,pressure),bd = 0,bg = 'white')
            
            lbl1.config(text = "Wind Speed")

            lbl2.config(text = "Humidity")

            lbl3.config(text = 'Description')
 
            lbl4.config(text = "Atmospheric Pressure")

            lbl6.config(text = "Temperature")

            lbl7.config(text = "Visibility")

            lbl8.config(text = "Minimum Temperature")

            lbl9.config(text = "Maximum Temperature")

            lbl10 .config(text = "Clouds")
            
            lbl11.config(text = "Feels like")
            

        else:
            messagebox.showerror("","Unknown City")
                
        tz = TimezoneFinder()
        timezone = tz.timezone_at(lng = long,lat = lati)
        zone = pytz.timezone(timezone)
        time = datetime.now(zone)
        c_t.config(text = f"In {city}\n{time.strftime('%I:%M %p')}")
        
        if 'list' in data:
            timestamp = data['list'][9]['dt']
            tim1 = datetime.fromtimestamp(timestamp,zone)
            clock.config(text = f"{tim1.strftime('%A')} In {city} ")
        
            tempe = int(data['list'][9]['main']['temp'])
           
            icon = data['list'][9]['weather'][0]['icon']
            the_icons = PhotoImage(file = f"{icon}@2x.png")
            lbl_icn.config(image = the_icons,bg = 'white',height = 50,width = 60)
            lbl_icn.image = the_icons
            
            forecast_temp.config(text = f"Temperature\n{tempe}°C")
        
            humi = int(data['list'][9]['main']['humidity'])
        
            forecast_hum.config(text = f'Humidity\n{humi}%')
        
            description = data['list'][9]['weather'][0]['description']
        
            forecast_des.config(text = f"Description\n{description}")
        
            wind = int(data['list'][9]['wind']['speed']*3.6)
            forecast_wind.config(text = f"Wind Speed\n{wind}km/h")
            
            cloud = data['list'][9]['clouds']['all']
            cloud_lbl.config(text = f"Clouds\n {cloud}%")
            print(data['list'][9]['dt_txt'])
            
            timestamp2 = data['list'][17]['dt']
            tim2 = datetime.fromtimestamp(timestamp2,zone)
            clock2.config(text = f"{tim2.strftime('%A')} In {city}")
            tempe2 = int(data['list'][17]['main']['temp'])
            forecast_day2_temp.config(text = f"Temperature\n {tempe2}°C")
            hum2 = data['list'][17]['main']['humidity']
            forecast_day2_hum.config(text = f"Humidity\n {hum2}%")
            description2 = data['list'][17]['weather'][0]['description']
            forecast_day2_description.config(text = f"Description\n {description2}")
            icon = data['list'][17]['weather'][0]['icon']
            w_icn = PhotoImage(file = f"{icon}@2x.png")
            icn2_label.config(image = w_icn,bg = 'white',activebackground = 'black',height = 50,width = 60)
            icn2_label.image = w_icn
            wind_speed = int(data['list'][17]['wind']['speed']*3.6)
            forecast_day2_wind_speed.config(text = f"Wind Speed\n {wind_speed}km/h")
            cloud2 = data['list'][17]['clouds']['all']
            cloud2_lbl.config(text = f"Clouds\n {cloud2}%")
            print(data['list'][17]['dt_txt'])
            '''
            timestamp3 = data['list'][25]['dt']
            tim3 = datetime.fromtimestamp(timestamp3,zone)
            clock3.config(text = f"{tim3.strftime('%A')} In {city}")
            tempe3 = int(data['list'][25]['main']['temp'])
            forecast_day3_temp.config(text = f"Temperature\n {tempe3}°C")
            hum3 = data['list'][25]['main']['humidity']
            forecast_day3_hum.config(text = f"Humidity\n {hum3}%")
            description3 = data['list'][25]['weather'][0]['description']
            forecast_day3_description.config(text = f"Description\n {description3}")
            icon = data['list'][25]['weather'][0]['icon']
            w_icn = PhotoImage(file = f"{icon}@2x.png")
            icn3_label.config(image = w_icn,bg = 'white',activebackground = 'black',height = 50,width = 60)
            icn3_label.image = w_icn
            wind_speed = int(data['list'][25]['wind']['speed']*3.6)
            forecast_day3_wind_speed.config(text = f"Wind Speed\n {wind_speed}km/h")
            cloud3 = data['list'][25]['clouds']['all']
            cloud3_lbl.config(text = f"Clouds\n {cloud3}%")
            print(cloud3)
            '''
            
        if 'list' in air_quality_data:
            time = air_quality_data['list'][0]['dt']
            print(time)
            aqi = air_quality_data['list'][0]['main']['aqi']
            aqi_viewer.config(text = f"Air Quality Index(AQI): {aqi}")
            co = air_quality_data['list'][0]['components']['co']
            co_lbl.config(text = f'CO : {co} µg/m³')
            no2 = air_quality_data['list'][0]['components']['no2']
            no2_lbl.config(text = f'NO₂ : {no2} µg/m³')
            no = air_quality_data['list'][0]['components']['no']
            no_lbl.config(text = f"NO : {no} µg/m³")
            so2 = air_quality_data['list'][0]['components']['so2']
            so_lbl.config(text = f"SO₂ : {so2} µg/m³")
            o3 = air_quality_data['list'][0]['components']['o3']
            o3_lbl.config(text = f"O₃ : {o3} µg/m³")
            pm2_5 = air_quality_data['list'][0]['components']['pm2_5']
            pm2_5_lbl.config(text = f"PM2.5 : {pm2_5} µg/m³")
            if aqi >= 3:
                bad_quality.config(text = f"Current Air Quality in {city}(Unhealthy)")
            if aqi < 3:
                bad_quality.config(text = f"Current Air Quality in {city}(Good)")
            
                
            alert_link = f"https://api.openweathermap.org/data/2.5/onecall?lat={lati}&lon={long}&appid=644be7103a977fa6cc8f498edaff9983"
            alert_data = req.get(alert_link).json()
            alert = alert_data.get('alerts')
            if alert:
                the_alert = alert.get('event')
                alert_lbl.config(text = f"{the_alert} is coming",fg = 'red')
            else:
                alert_lbl.config(text = "No alert",fg = 'green',bg = "black")
    def get_weather():        
        city = cityentry.get()
        threading.Thread(target = weather , args = (city,)).start()
        
    def current_location():
        global city_now
        TOKEN = "b6499ca52d5fc1"
        url = f"https://ipinfo.io/json?token={TOKEN}"
        response = req.get(url)
        data = response.json()
    
        city_now = data.get('city')
        loc = data.get('loc', '')
        lat, lon = map(float, loc.split(',')) if loc else (None, None)

        print("City:", city_now)
        print("Latitude:", lat)
        print("Longitude:", lon)
        threading.Thread(target=weather,args=(city_now,)).start()


 
        
    
        
        
        
    weather_translation = {
        
        "Clear": "সুপরিস্কার",
        "Clouds": "মেঘলা",
        "Rain": "বৃষ্টি",
        "Drizzle": "হালকা বৃষ্টি",
        "Thunderstorm": "বজ্রপাত",
        "Snow": "তুষারপাত",
        "Mist": "কুয়াশা",
        "Haze": "ধোঁয়াটে",
        "Fog": "কুয়াশাচ্ছন্ন",
        "Smoke": "ধোঁয়া",
        "Dust": "ধুলা",
        "Sand": "বালু",
        "Ash": "চুনা",
        "Squall": "ঝড়",
        "Tornado": "সিক্লোন"
        }


    def speak_weather_bangla(city,condition, temp, feels_like,humidity, wind_speed,pressure):
        def run_tts():
            link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=644be7103a977fa6cc8f498edaff9983"
            the_data = req.get(link).json()

            condition = the_data['weather'][0]['main']
            city_name = the_data['name']
            temp = the_data['main']['temp']
            feels_like = the_data['main']['feels_like']
            humidity = the_data['main']['humidity']
            wind_speed = int(the_data['wind']['speed']*3.6)
            pressure = the_data['main']['pressure']

            condition_bn = weather_translation.get(condition, condition)

            text_bn = (
                f"আজ {city_name}-এ আবহাওয়া {condition_bn}। "
                f"তাপমাত্রা {temp} ডিগ্রি সেলসিয়াস, "
                f"শরীর অনুভূতি {feels_like} ডিগ্রি। "
                f"আর্দ্রতা {humidity} শতাংশ। "
                f"বাতাসের গতি {wind_speed} কিমি প্রতি ঘণ্টা। "
                f"বায়ুচাপ {pressure} হেক্টোপ্যাস্কাল।"
            )

            filename = f"weather_{city_name}.mp3"
            tts = gTTS(text=text_bn, lang='bn')
            tts.save(filename)

            os.system(f"start {filename}")

        threading.Thread(target=run_tts).start()

        
        
        
    def button(event):
        if event.keysym == 'Return':
            get_weather()
    def speech():
        def c():
            listen.config(text = '')
        def recognize():
            
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source,duration = 1)
                listen.config(text = 'Listening...')
                audio = recognizer.listen(source)
                try:
                    city = recognizer.recognize_google(audio)
                    weather(city)
                except:
                    messagebox.showerror('',"I can't understand")
                    listen.after(2000,c)
                listen.after(2000,c)
        
        threading.Thread(target = recognize).start()
    def celcius(event):
        temp = int(weather_data['main']['temp'])
        t.config(text = f"{temp}°C")
            
        feelings = int(weather_data['main']['feels_like'])
        feeling_temp.config(text = f"{feelings}°C")
            
        tempe = int(data['list'][7]['main']['temp'])
        forecast_temp.config(text = f'Temperature\n{tempe}°C')
        tempe2 = int(data['list'][15]['main']['temp'])
        forecast_day2_temp.config(text = f"Temperature\n {tempe2}°C")
        
        max_tempe = int(weather_data['main']['temp_max'])
        max_temp.config(text = f'{max_tempe}°C')
            
        min_tempe = int(weather_data['main']['temp_min'])
        min_temp.config(text = f'{min_tempe}°C')
        
    def fahrenheit(event):
        
        temp = int(weather_data['main']['temp']*(1.8)+32)
        t.config(text = f"{temp}°F")
            
        feelings = int(weather_data['main']['feels_like']*(1.8)+32)
        feeling_temp.config(text = f"{feelings}°F")
            
        tempe = int(data['list'][7]['main']['temp']*(1.8)+32)
        forecast_temp.config(text = f"Temperature\n{tempe}°F")
        
        tempe2 = int(data['list'][15]['main']['temp']*(1.8)+32)
        forecast_day2_temp.config(text = f"Temperature\n {tempe2}°F")
        
        max_tempe = int(weather_data['main']['temp_max']*(1.8)+32)
        max_temp.config(text = f'{max_tempe}°F')
            
        min_tempe = int(weather_data['main']['temp_min']*(1.8)+32)
        min_temp.config(text = f'{min_tempe}°F')
    def kelvin(event):
        
        temp = int(weather_data['main']['temp']+273.15)
        t.config(text = f"{temp}°K")
            
        feelings = int(weather_data['main']['feels_like']+273.15)
        feeling_temp.config(text = f"{feelings}°K")
            
        tempe = int(data['list'][7]['main']['temp']+273.15)
        forecast_temp.config(text = f"Temperature\n{tempe}°K")
        
        tempe2 = int(data['list'][15]['main']['temp']+273.15)
        forecast_day2_temp.config(text = f"Temperature\n {tempe2}°K")
        
        max_tempe = int(weather_data['main']['temp_max']+273.15)
        max_temp.config(text = f'{max_tempe}°K')
            

        min_tempe = int(weather_data['main']['temp_min']+273.15)
        min_temp.config(text = f'{min_tempe}°K')
    def integer(event):
        temp = int(weather_data['main']['temp'])
        t.config(text = f"{temp}°C")
        feelings = int(weather_data['main']['feels_like'])
        feeling_temp.config(text = f"{feelings}°C")
        tempe = int(data['list'][7]['main']['temp'])
        forecast_temp.config(text = f"Temperature\n{tempe}°C")
        tempe2 = int(data['list'][15]['main']['temp'])
        forecast_day2_temp.config(text = f"Temperature\n {tempe2}°C")
        max_tempe = int(weather_data['main']['temp_max'])
        max_temp.config(text = f'{max_tempe}°C')
            
        min_tempe = int(weather_data['main']['temp_min'])
        min_temp.config(text = f'{min_tempe}°C')
        
    def floating(event):
        temp = weather_data['main']['temp']
        t.config(text = f"{temp}°C")
        feelings = weather_data['main']['feels_like']
        feeling_temp.config(text = f"{feelings}°C")
        tempe = data['list'][7]['main']['temp']
        forecast_temp.config(text = f"Temperture\n{tempe}°C")
        tempe2 = data['list'][15]['main']['temp']
        forecast_day2_temp.config(text = f"Temperature\n {tempe2}°C")
        max_tempe = weather_data['main']['temp_max']
        max_temp.config(text = f'{max_tempe}°C')
            
        min_tempe = weather_data['main']['temp_min']
        min_temp.config(text = f'{min_tempe}°C')
    def microphone_start(event):
        speech()
    def make_map():
        obj = Map(location=[23.8103, 90.4125], zoom_start=6)
        TileLayer(
            tiles = "https://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{y}.png?appid=644be7103a977fa6cc8f498edaff9983",
            attr = "OpenWeatherMap").add_to(obj)
        obj.save('map.html')
        print('svd')
    def show_temp_map():
        make_map()
        gui.destroy()
        web.create_window("Map","map.html")
        web.start()
        
    def widget():
        web.create_window("Widget Home City Khulna","aiub.html")
        web.start()
    def update_needle(angle):
        canvas.delete("needle")
        angle_rad = math.radians(angle)
        x_end = center_x + needle_length * math.cos(angle_rad)
        y_end = center_y - needle_length * math.sin(angle_rad)
        canvas.create_line(center_x, center_y, x_end, y_end, fill="red", width=2, tag="needle")
        
        
    def ai():
        global first_message
        
        gemini.configure(api_key='AIzaSyAcMSjAMfHbH-WLHdoJTIkz8SoWMe8e64w')
    
        conversation_history = []

        first_message = True
    
        
        def ask_weather(user_input):

            conversation_history.append({"role": "user", "content": user_input})


            history_text = ""
            for message in conversation_history:
                history_text += f"{message['role']}: {message['content']}\n"

            full_prompt = f"""
        You are a weather assistant. Only answer about the weather of any city in the world fully detailed.if user tells to udtae be updated as user wants.if your user tells you to browse any web related to cultivation and weather visity and give the data to them.answer their greetings also and remember you're not gemini anymore now.you're abohawa.Answer about forecasts fully detailed also. Suggest crop cultivation advice based on weather if asked.
        Be respectful, use translations if requested. If the user asks something unrelated, respond politely: "I only provide weather information.Show graphical data if user wants.generate image if user wants and give them a link to the generated image as you want.But remember that all the data given must be taken from the openweathermap web"

        Conversation history:
        {history_text}
        Assistant:
        """

            try:
                model = gemini.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content(full_prompt)
            except Exception:
                model = gemini.GenerativeModel("gemini-pro")
                response = model.generate_content(full_prompt)
            answer = response.text

            conversation_history.append({"role": "assistant", "content": answer})
            return answer

        def send_message():
            global first_message
            user_input = entry.get().strip()


            chat_window.configure(state='normal')

            if first_message:
                
                chat_window.delete("1.0",END)
                first_message = False
                
            chat_window.configure(state='normal')
            chat_window.insert(END, f"You: {user_input}\n")
            chat_window.configure(state='disabled')
            entry.delete(0,END)

            response = ask_weather(user_input)
            chat_window.configure(state='normal')
            chat_window.insert(END, f"Abohawa: {response}\n\n")
            chat_window.configure(state='disabled')
            chat_window.see(END)

        gui = Tk()
        gui.title("🌤 Abhohawa")

        gui.geometry("600x500")
        gui.configure(bg="#1E1E2F")

        chat_window = scrolledtext.ScrolledText(
            gui, wrap=WORD, state='normal', font=("Arial", 12),
            bg="#2E2E3E", fg="white"
        )
        chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        chat_window.insert(END, " Abhohawa powered by Gemini and Openweathermap")
        chat_window.tag_add("center", "1.0", "end")
        chat_window.tag_configure("center", justify='center', font=("Arial", 14, "bold"))
        chat_window.config(state='disabled')

        frame = Frame(gui, bg="#1E1E2F")
        frame.pack(padx=10, pady=10, fill=X)

        entry = Entry(frame, font=("Arial", 12), bg="#3E3E50", fg="white")
        entry.pack(side=LEFT, fill=X, expand=True, padx=(0,10))
        entry.bind("<Return>", lambda event: send_message())

        send_button = Button(frame, text="Send", command=send_message, bg="#4E9AF1", fg="white", bd=0)
        send_button.pack(side=RIGHT)

        gui.mainloop()
        
    def get_data():
        get_weather(city)
        
    

        
    

    gui = Tk()
    gui2 = CTk()
    gui.title("Weather")
    gui.geometry("1300x680")
    

    search = PhotoImage(file = 'searchb.png')
    Label(gui,image = search,bg = 'white').place(x = 600,y= 50)
    searchbtn = PhotoImage(file = 'searchico.png')
   
    microphone = PhotoImage(file = 'mic4.png')
    
    cityentry = Entry(gui,bg = '#404040',fg = 'white',font = ('Helvetica',18),bd = 0,justify="center")
    cityentry.place(x = 675, y = 72)
    cityentry.focus()

    icn = PhotoImage(file = '02d@2x.png')
    gui.iconphoto(False,icn)

    
    sun = PhotoImage(file = 'sun1.png')
    

    listen = Label(gui,text = '',bg = 'white',fg = 'Black',font = ('Helvetica',20,))
    listen.place(x = 50, y= 90)

    c_t = Label(gui,text = '',font = ('Helvetica',20),bg = 'white')
    c_t.place(x = 1100,y = 150)

    frame1 = Frame(gui,height = 200,width = 350)
    frame1.place(x = 100, y= 290)
    lbl_icn = Label(gui)
    lbl_icn.place(x = 300,y = 350)
    clock = Label(gui,text = "...",fg = 'black',font = ("Helvetica",15,'bold'))
    clock.place(x = 100, y = 300 )
    forecast_temp = Label(gui,text = '...',fg = 'black')
    forecast_temp.place(x = 100,y = 400 )
    forecast_hum = Label(gui,text = '...',fg = 'black')
    forecast_hum.place(x = 200,y = 400)
    forecast_des = Label(gui,text = '...',fg = 'black')
    forecast_des.place(x = 100,y = 450)
    forecast_wind = Label(gui,text = '...',fg = 'black')
    forecast_wind.place(x = 200, y = 450)
    cloud_lbl = Label(gui,text = '...',fg = 'black')
    cloud_lbl.place(x = 350,y = 450)
    
    frame2 = Frame(gui,height = 200,width = 350)
    frame2.place(x = 500,y = 290)

    
    icn2_label = Label(gui)
    icn2_label.place(x = 700, y = 350)
    clock2 = Label(gui,text = "...",fg = 'black',font = ("Helvetica",15,"bold"))
    clock2.place(x = 500, y = 300)
    forecast_day2_temp = Label(gui,text = "...",fg = 'black')
    forecast_day2_temp.place(x = 500, y = 400)
    forecast_day2_hum = Label(gui,text = '...',fg = 'black')
    forecast_day2_hum.place(x = 600, y= 400)
    forecast_day2_description = Label(gui,text = '...',fg = 'black')
    forecast_day2_description.place(x = 500, y = 450)
    forecast_day2_wind_speed = Label(gui,text = '...',fg = 'black')
    forecast_day2_wind_speed.place(x = 600 , y = 450)
    cloud2_lbl = Label(gui,text = '...',fg = 'black')
    cloud2_lbl.place(x = 750,y = 450)
    
    
    clock3 = Label(gui,text = "...",fg = 'black',font = ("Helvetica",15,"bold"))
    clock3.place(x = 100000, y = 300)
    
    
    frame3 = Frame(gui,height = 200,width = 350)
    frame3.place(x = 900,y = 290)
    aqi_viewer = Label(gui,text = '...',fg = 'black')
    aqi_viewer.place(x = 900,y = 450)
    co_lbl = Label(gui,text ='...')
    co_lbl.place(x = 900,y = 400)
    no2_lbl = Label(gui,text = '...',fg = 'black')
    no2_lbl.place(x = 1150, y = 450)
    no_lbl = Label(gui,text = '...',fg = 'black')
    no_lbl.place(x = 1150,y = 400)
    so_lbl = Label(gui,text = '...',fg = 'black')
    so_lbl.place(x = 900,y = 350)
    o3_lbl = Label(gui,text = '...',fg = 'black')
    o3_lbl.place(x =1150 , y = 350)
    pm2_5_lbl = Label(gui,text = '...',fg = 'black')
    pm2_5_lbl.place(x = 900, y=325)
    bad_quality = Label(gui,text = '...',fg = 'black',font = ('Helvetica',10,'bold'))
    bad_quality.place(x = 900,y = 300)
    
    alert_lbl = Label(gui,text = "",fg = 'white')
    alert_lbl.place(x = 1200,y = 900)
    
    sunrise_lbl = Label(gui,text = '',fg = 'black',font = ('helvetica',10,'bold'),bg = 'white')
    sunrise_lbl.place(x =50,y = 230)
    sunset_lbl = Label(gui,text = '',fg = 'black',font = ('helvetica',10,'bold'),bg = 'white')
    sunset_lbl.place(x = 50, y = 250)
    
            

    frame_crnt_w = Frame(gui,height = 200 , width = 650)
    frame_crnt_w.place(x = 100, y = 500)
    lbl_crnt = Label(gui,text = f"...",font = ("Helvetica",15,'bold'))
    lbl_crnt.place(x = 100, y= 500)
    
    lbl1 = Label(gui,text = "",bd = 0 ,fg = "black")
    lbl1.place(x = 100, y = 550)
    lbl2 = Label(gui,text = "")
    lbl2.place(x = 300, y = 550)
    lbl3 = Label(gui,text = '')
    lbl3.place(x = 400,y =  550)
    lbl4 = Label(gui,text = "")
    lbl4.place(x = 500,y  = 550)
    lbl6 = Label(gui,text = "")
    lbl6.place(x = 200,y = 550)
    lbl7 = Label(gui,text = "")
    lbl7.place(x = 100,y = 600)
    lbl8 = Label(gui,text = "")
    lbl8.place(x = 100,y = 650)
    lbl9 = Label(gui,text = "")
    lbl9.place(x = 400,y = 650)
    lbl10 = Label(gui,text = "")
    lbl10.place(x = 300,y = 600)
    lbl11 = Label(gui,text = "")
    lbl11.place(x = 200,y = 600)
    lbl_sun = Label(gui,bd = 0)
    lbl_sun.place(x = 100, y= 750)
    
    
    location_img = PhotoImage(file = 'local.png')
    
    first_l = Label(text = '...',fg = 'black',font=(('Seoge UI',20,'bold')) )
    t = Label(gui,text = '...')
    t.place(x = 200, y = 565)
    w = Label(gui,text = '...')
    w.place(x = 100, y= 565)
    h = Label(gui,text = '...')
    h.place(x = 300, y= 565)
    d = Label(gui,text = '...')
    d.place(x = 400,y = 565)
    p = Label(gui,text = '...')
    p.place(x = 500, y = 565)
    visibility= Label(gui,text = '...')
    visibility.place(x =100 , y=620)
    min_temp = Label(text = '...')
    min_temp.place(x = 100,y = 670)
    max_temp = Label(gui,text = '...')
    max_temp.place(x = 400,y = 670)
    clouds = Label(gui,text = '...')
    clouds.place(x = 300,y = 620)
    feeling_temp = Label(gui,text = '...')
    feeling_temp.place(x = 200, y = 620)
    sunrise_optional_lbl = Label(gui,text = "...")
    sunrise_optional_lbl.place(x = 400,y = 600)
    
    sunset_optional_lbl = Label(gui,text = "...")
    sunset_optional_lbl.place(x  = 600,y = 600)
    
    
    
    canvas_size = 80 
    center_x = canvas_size // 2
    center_y = canvas_size // 2
    needle_length = canvas_size // 8

    canvas = Canvas(gui, width=canvas_size, height=canvas_size,bg=gui.cget("bg"), bd=0)
    canvas.place(x=600, y=632)

    canvas.create_oval(center_x - 30, center_y - 30, center_x + 30, center_y + 30, outline="black", width=1)

    directions = {
        'N': (center_x, center_y - 20),
        'E': (center_x + 20, center_y),
        'S': (center_x, center_y + 20),
        'W': (center_x - 20, center_y)
    }

    for direction, (x, y) in directions.items():
        canvas.create_text(x, y, text=direction, font=("Segoe UI", 8))


    
    
    
    
    lbl5 = Label(gui,text = "Select your scale from below\n (Default is Celcius)",font = ('helvetica',15),bg = 'white',fg = 'black', bd = 0)
    lbl5.place(x = 1040,y = 0)
    
    val = ['Integer','Floating']
    combobox2 = ttk.Combobox(gui,value = val,font = ('Helvetica',10,'bold'))
    combobox2.place(x = 1100, y= 100)
    combobox2.bind('<<ComboboxSelected>>',values)
    value = ['Fahrenheit','Kelvin','Celsius']
    combobox = ttk.Combobox(gui,values = value,font = ('Helvetica',10,'bold'))
    combobox.place(x = 1100,y = 50)
    combobox.bind('<<ComboboxSelected>>',com)
    
    gui.bind("<Control-i>",integer)
    gui.bind("<Control-o>",floating)
    
    gui.bind('<KeyPress>',button)
    
    gui.bind("<Control-c>",celcius)
    
    gui.bind("<Control-k>",kelvin)
    
    gui.bind("<Control-f>",fahrenheit)
    
    gui.bind("<Control-m>",microphone_start)
    btn = Button(gui,image = searchbtn,command = get_weather,activebackground = 'white',bd = 0,cursor = 'hand2',bg = '#404040')
    btn.place(x = 970,y = 62)
    
    btn3 = Button(gui,image = microphone,command = speech,bd = 0,bg = 'white',activebackground = 'white')
    btn3.place(x = 500,y = 50)
    
    btn4 = Button(gui,text = 'view storm map',command = show_temp_map,bd = 0,bg = 'white')
    btn4.grid()
    
    btn_bng = Button(gui,text = '')
    btn_bng.grid()
    btn_ai = Button(gui,text = 'ai mode',command = ai)
    btn_ai.grid()
    
    current_location()
    

    
    gui.config(bg = 'white')
    gui.mainloop()
def close():
    gui.destroy()
    open()
    
gui = Tk()
gui.title('Weather')
gui.geometry('1000x600')
gui.resizable(False,False)
gui.config(bg = 'red')
icn = PhotoImage(file = 'sun1.png')
gui.iconphoto(False,icn)
gui.after(8500,close)
text = ""
txt = "সকল বীর শহিদদের স্মরণে"
label_text = Label(gui,text = txt,bg = 'red',fg = 'black',font = ('Helvetica',30,'bold'))
label_text.place(x = 200,y = 150)
a_label = Label(gui,text = 'الله أكبر',font = ('Helvetica',40),bg = 'green')
a_label.place(x = 400,y = 200)
count = 0
def anime():
    global text, count
    if count < len(txt):
        text += txt[count]                
        label_text.config(text=text)
        count += 1
        gui.after(320, anime)  
    else:
        
        gui.after(1000, reset_and_restart)

def reset_and_restart():
    global text, count
    text = ""
    count = 0
    label_text.config(text="")
    gui.after(500, anime)

close()

gui.mainloop()
