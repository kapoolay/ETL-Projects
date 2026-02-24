import pandas as pd

def transform_predictions(data):
    rows = []   # should not be in the loop
    for drow in data['data']:

        # vehicle data may be missing for future predictions, handle gracefully 
        try:
            vehicle_id = drow['relationships']['vehicle']['data']['id']
        except(KeyError, TypeError):
            vehicle_id = None

        r = {
            'arrival_time': drow['attributes']['arrival_time'],
            'departure_time': drow['attributes']['departure_time'],
            'direction_id': drow['attributes']['direction_id'],
            'stop_id': drow['relationships']['stop']['data']['id'],
            'trip_id': drow['relationships']['trip']['data']['id'],
            'vehicle_id': vehicle_id
            # 'vehicle_id': drow['relationships']['vehicle']['data']['id'],
        }

        rows.append(r)

    df = pd.DataFrame(rows)
    return df

if __name__ == "__main__":
    from extract import extract_predictions
    data = extract_predictions()
    df = transform_predictions(data)
    print(df)
