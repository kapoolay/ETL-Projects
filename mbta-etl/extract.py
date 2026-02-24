import requests

def extract_predictions():
    response = requests.get("https://api-v3.mbta.com/predictions?filter[stop]=place-jfk&filter[route]=Red")
    data = response.json()
    # print(data)
    return data

if __name__ == "__main__":
    data = extract_predictions()
    print(data)