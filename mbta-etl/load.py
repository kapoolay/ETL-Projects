import sqlite3
import pandas as pd

def load_predictions(df):
    conn = sqlite3.connect("predictions.db")
    df.to_sql("predictions", conn, if_exists="replace", index=False)
    conn.close()

if __name__ == "__main__":
    from extract import extract_predictions
    from transform import transform_predictions

    rawdata = extract_predictions()
    df = transform_predictions(rawdata)
    load_predictions(df)
    print("Data loaded successfully!")

    # preview database for loaded data
    conn = sqlite3.connect("predictions.db")
    result = pd.read_sql("select * from predictions limit 10", conn)
    conn.close()
    print(result)