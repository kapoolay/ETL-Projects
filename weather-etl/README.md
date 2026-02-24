# Weather ETL Pipeline

A Python pipeline that extracts hourly weather data from the Open-Meteo API,
transforms it using pandas, and loads it into a local SQLite database.
Runs automatically on a schedule using Windows Task Scheduler.

---

## Tools & Technologies

- Python 3.13
- requests - API calls
- pandas - data transformation
- SQLite - local data storage
- Windows Task Scheduler - automation

---

## Pipeline Overview

| Step | File | Description |
|------|------|-------------|
| Extract | `extract.py` | Calls Open-Meteo API and returns raw JSON |
| Transform | `transform.py` | Parses JSON into a pandas DataFrame |
| Load | `load.py` | Writes DataFrame to SQLite database |
| Orchestrate | `main.py` | Runs the full pipeline on a loop |

---

## How to Run Locally

1. Clone the repo
```
   git clone
   cd weather-etl
```

2. Create and activate a virtual environment
```
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies
```
   pip install -r requirements.txt
```

4. Run the pipeline
```
   python main.py
```

---

## Database Schema

Table: `weather`

| Column | Type | Description |
|--------|------|-------------|
| timestamp | TEXT | Hour of the forecast (YYYY-MM-DD HH:MM:SS) |
| temperature_c | REAL | Temperature in Celsius |

---

## Sample Output
```
          timestamp  temperature_c
0  2026-02-18 00:00:00            5.2
1  2026-02-18 01:00:00            3.9
2  2026-02-18 02:00:00            3.1
```

---

## Future Improvements?

- Switch from `replace` to `append` mode with `INSERT OR IGNORE` to build
  historical data over time
- Add more weather fields (wind speed, precipitation, humidity)
- Export data to CSV for reporting