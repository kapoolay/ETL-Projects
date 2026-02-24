import sqlite3
import pandas as pd

def load_weather(df):
    conn = sqlite3.connect("weather.db")

    df.to_sql("weather", conn, if_exists="replace", index=False)

    conn.close()

if __name__ == '__main__':
    from transform import transform_weather
    from extract import extract_weather

    # For testing
    raw = extract_weather()
    df = transform_weather(raw)
    load_weather(df)
    print("Data loaded successfully!")

    # preview database to make sure data is saved
    conn = sqlite3.connect("weather.db")
    result = pd.read_sql("select count(*) from weather limit 5", conn)
    conn.close()
    print(result)