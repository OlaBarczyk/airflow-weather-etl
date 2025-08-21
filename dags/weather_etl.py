from airflow import DAG
from airflow.decorators import task
from datetime import datetime
from pathlib import Path
import csv
import requests  # <-- prawdziwe API

# DAG
with DAG(
    dag_id="weather_etl",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",     # na razie raz dziennie; później można zmienić na "0 * * * *"
    catchup=False,
    tags=["etl", "weather"],
):
    # EXTRACT: pobiera ostatnią godzinę pogody z Open-Meteo (Warszawa)
    @task(retries=2)
    def extract() -> dict:
        lat = 52.2297
        lon = 21.0122
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m,relative_humidity_2m,pressure_msl,precipitation",
            "timezone": "UTC",
        }

        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()

        i = -1  # ostatnia dostępna godzina
        rec = {
            "city": "Warsaw",
            "ts_utc": data["hourly"]["time"][i],
            "temp_c": data["hourly"]["temperature_2m"][i],
            "humidity_pct": data["hourly"]["relative_humidity_2m"][i],
            "pressure_hpa": data["hourly"]["pressure_msl"][i],
            "precip_mm": data["hourly"]["precipitation"][i],
        }
        return rec

    # TRANSFORM: na razie nic nie zmienia (miejsce na walidacje/reguły jakości)
    @task
    def transform(record: dict) -> dict:
        # przykład walidacji minimalnej:
        # jeśli temperatura jest nietypowa, możesz rzucić wyjątek:
        # if record["temp_c"] < -80 or record["temp_c"] > 70:
        #     raise ValueError("Out-of-range temperature")
        return record

    # LOAD: dopisuje rekord do CSV (tworzy plik/nagłówek jeśli trzeba)
    @task
    def load(record: dict) -> str:
        out_dir = Path(__file__).parent / "output"
        out_dir.mkdir(parents=True, exist_ok=True)
        csv_path = out_dir / "weather.csv"

        write_header = not csv_path.exists()
        with csv_path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=record.keys())
            if write_header:
                writer.writeheader()
            writer.writerow(record)

        return str(csv_path)

    # kolejność zadań
    load(transform(extract()))
