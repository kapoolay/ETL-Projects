from extract import extract_weather
from transform import transform_weather
from load import load_weather
import sqlite3
import pandas as pd
import time

def main():
    print('Extracting...')
    raw = extract_weather()
    print('Transforming...')
    df = transform_weather(raw)
    print('Loading...')
    load_weather(df)
    print('ETL COMPLETED!')

    # preview database to make sure data is saved
    conn = sqlite3.connect("weather.db")
    top5 = pd.read_sql("select * from weather limit 5", conn)
    conn.close()
    print(top5)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(3600)

