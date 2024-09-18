# Importing required libraries
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily, Monthly
from statistics import mean
import os
from twilio.rest import Client

def collect_weather(lat, long):
    # Set time period
    start = datetime(2022, 1, 1)
    end = datetime(2022, 12, 31)

    # Create Point
    location = Point(lat, long)

    # Get daily data for 2022
    data = Daily(location, start, end)
    data = data.fetch()
    try:
        temp_avg = mean(data["tavg"])
        prcp_avg = sum(data["prcp"])
        return temp_avg, prcp_avg
    except:
        print("No weather data found")
        return None, None

def send_sms(message_body, to_phno):
    account_sid = 'ACa1724f4ca98de87b1ed387eec79e157d'
    auth_token = 'a6c361f875a5aae76d112f0a2db09810'
    
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body=message_body,
                     from_='+18335095612',
                     to=to_phno
                 )
    print(message.sid)

def main_messaging(lat, long, to_phno):
    temperature, precipitation = collect_weather(lat, long)
    
    if temperature and precipitation:
        message_body = f'Average Temperature for today: {temperature:.2f}°C\nTotal Precipitation for today: {precipitation:.2f}mm'
        send_sms(message_body, to_phno)
    else:
        print("Failed to fetch weather data.")
