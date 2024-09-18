def get_region(latitude, longitude):
    if 24 <= latitude <= 37 and -87 <= longitude <= -80:
        return "Southeast"
    elif 24 <= latitude <= 37 and -105 <= longitude <= -87:
        return "Southcentral"
    elif 24 <= latitude <= 37 and -125 <= longitude <= -105:
        return "Southwest"
    elif 37 <= latitude <= 49 and -87 <= longitude <= -67:
        return "Northeast"
    elif 37 <= latitude <= 49 and -125 <= longitude <= -105:
        return "Northwest"
    elif 37 <= latitude <= 49 and -105 <= longitude <= -87:
        return "Midwest"
    elif 18 <= latitude <= 23 and -160 <= longitude <= -154:
        return "Hawaii"
    elif 51 <= latitude <= 72 and -179 <= longitude <= -129:
        return "Alaska"
    else:
        return "National"

if __name__=='__main__':
    # Example coordinates for testing
    coordinates = [
        (34.0522, -118.2437),  # Los Angeles, California (Southwest)
        (32.7767, -96.7970),   # Dallas, Texas (Southcentral)
        (40.7128, -74.0060),   # New York City, New York (Northeast)
        (41.8781, -87.6298),   # Chicago, Illinois (Midwest)
        (25.7617, -80.1918),   # Miami, Florida (Southeast)
        (61.2181, -149.9003),  # Anchorage, Alaska (Alaska)
        (21.3069, -157.8583),  # Honolulu, Hawaii (Hawaii)
        (39.9042, -104.9788),  # Denver, Colorado (National)
    ]

    for lat, lon in coordinates:
        region = get_region(lat, lon)
        print(f"Latitude: {lat}, Longitude: {lon} -> Region: {region}")
