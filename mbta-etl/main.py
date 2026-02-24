from extract import extract_predictions
from transform import transform_predictions
from load import load_predictions
import sqlite3
import pandas as pd

def main():
    print("Extracting...")
    rawdata = extract_predictions()

    print("Transforming...")
    df = transform_predictions(rawdata)

    print("Loading...")
    load_predictions(df)

    print("ETL COMPLETE!")

    # Preview db
    conn = sqlite3.connect("predictions.db")
    preview = pd.read_sql("select * from predictions limit 5", conn)
    conn.close()
    print(preview)

if __name__ == "__main__":
    main()