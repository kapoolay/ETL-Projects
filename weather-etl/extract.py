import requests

def extract_weather():
    # NY
    lat = 40.7128
    lon = -74.0060

    response = requests.get("https://api.open-meteo.com/v1/forecast", 
                 params={
                     'latitude': lat,
                     'longitude': lon,
                     'hourly': "temperature_2m"
                 })
    
    data = response.json()
    # preview API response
    # print(data)
    return data

if __name__ == "__main__":
    extract_weather()