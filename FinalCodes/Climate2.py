# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily, Monthly
from statistics import mean

def collect_weather(lat, long):
    # Set time period
    start = datetime(2022, 1, 1)
    end = datetime(2022, 12, 31)

    # Create Point for Vancouver, BC
    location = Point(lat, long)

    # Get daily data for 2018
    data = Monthly(location, start, end)
    data = data.fetch()
    try:
        temp_avg = mean(data["tavg"])
        prcp_avg = sum(data["prcp"])
        return temp_avg, prcp_avg/10
    except:
        print("No weather data found")
        return None, None


if __name__ == '__main__':
    temperature, precipitation = collect_weather(41.06104324059672, -81.51734366383978)

    print(temperature, precipitation)