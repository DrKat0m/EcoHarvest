import requests
from datetime import datetime, timedelta

def get_historical_weather(api_key, location, start_date, end_date):
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

    params = {
        "key": api_key,
        "location": location,
        "startDateTime": start_date.strftime("%Y-%m-%dT%H:%M:%S"),
        "endDateTime": end_date.strftime("%Y-%m-%dT%H:%M:%S"),
        "unitGroup": "metric",
        "include": "daily",
        "contentType": "json"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching historical weather data.")
        return None

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your Visual Crossing Weather Data API key
    api_key = "VY73J6EZ2RZNSPRNM62JAZFRR"
    location = "New York, NY"  # Replace with your desired city and country
    end_date = datetime.now()
    start_date = end_date - timedelta(days=50)  # Retrieve data for the past year
    print(end_date, start_date)
    print("---------------------")

    historical_data = get_historical_weather(api_key, location, start_date, end_date)
    print(historical_data)
    print('------------------------')
    records = historical_data['days']
    print(len(records))
    if historical_data:
        for record in records:
            print(record)
            '''
            max_temp = records[1]
            min_temp = record[2]
            precipitation = record[3]
            humidity = record[4]
            '''
            #print(f"{date}\t{max_temp}\t\t{min_temp}\t\t{precipitation}\t\t\t{humidity}")