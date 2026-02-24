# MBTA Transit ETL Pipeline

A Python ETL pipeline that pulls real-time Red Line arrival predictions from the MBTA V3 API at JFK/UMass station and stores them in a local SQLite database.

## What It Does

- **Extract** — Calls the MBTA V3 API for live Red Line predictions
- **Transform** — Parses and cleans the JSON response into a pandas DataFrame
- **Load** — Stores the cleaned data in a local SQLite database

## Tech Stack

- Python 3
- `requests` — API calls
- `pandas` — data transformation
- `sqlite3` — local database storage

## Project Structure

```
mbta-etl/
├── extract.py
├── transform.py
├── load.py
├── main.py
├── predictions.db
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repo and navigate into the project folder
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the full pipeline:

```
python main.py
```

This will extract, transform, and load the latest predictions into `predictions.db`, then print a preview of the data.

## Data Fields

| Field | Description |
|---|---|
| arrival_time | Predicted arrival time |
| departure_time | Predicted departure time |
| direction_id | 0 = Southbound, 1 = Northbound |
| stop_id | MBTA stop identifier |
| trip_id | Trip identifier |
| vehicle_id | Assigned vehicle (if available) |

## API

Uses the [MBTA V3 API](https://api-v3.mbta.com) — no API key required.
