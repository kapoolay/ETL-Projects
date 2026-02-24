# ETL Projects

A collection of Python ETL pipeline projects demonstrating real-world data engineering skills including API integration, data transformation, and local data storage.

## Projects

| Project | Description | API | Storage |
|---|---|---|---|
| [MBTA Transit ETL](./mbta-etl) | Pulls real-time Red Line predictions at JFK/UMass | MBTA V3 | SQLite |
| [NFL Fantasy ETL](./nfl-fantasy-etl-pipeline) | Extracts NFL player stats and calculates fantasy football scores by week | ESPN API / Web Scraping | SQLite |
| [Weather ETL](./weather-etl) | Pulls real-time weather data and stores forecasts | Open-Meteo | SQLite |

## Tech Stack

- Python 3
- `requests` — API calls
- `pandas` — data transformation
- `sqlite3` — local data storage

## Structure

Each project follows the same modular ETL structure:

```
project/
├── extract.py      # API call
├── transform.py    # clean and structure data
├── load.py         # store to SQLite
├── main.py         # orchestration
├── requirements.txt
└── README.md
```

## Running a Project

Navigate into any project folder and follow the README instructions there.

---

*More projects coming soon.*
