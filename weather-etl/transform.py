import pandas as pd

def transform_weather(raw_data):
    timestamp = raw_data['hourly']['time']
    temperature_c = raw_data['hourly']['temperature_2m']

    df = pd.DataFrame({
        'timestamp': timestamp,
        'temperature_c': temperature_c
    })

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    return df

if __name__ == "__main__":
    from extract import extract_weather
    raw_data = extract_weather()
    df = transform_weather(raw_data)
    print(df.head())