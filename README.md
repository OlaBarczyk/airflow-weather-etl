# 🌤️ Airflow Weather ETL (Open-Meteo + CSV)

## 📌 Project Overview  
This project demonstrates a simple **ETL pipeline in Apache Airflow** that fetches weather data from the free **[Open-Meteo API](https://open-meteo.com/)** and stores it in **CSV format**.  
The pipeline can be extended with transformations and data loading into **PostgreSQL** or other data warehouses.  

---

## ⚙️ Features
- Fetches weather data (temperature, humidity, pressure, etc.) from Open-Meteo API  
- Runs automatically as an Airflow DAG  
- Saves results to a CSV file (`/dags/output/weather.csv`)  
- Easily extendable for database integration  

---

## 📂 Project Structure
├── dags/ # Airflow DAG files
│ ├── weather_etl.py # Main ETL DAG fetching weather data
│ └── exampledag.py # Example DAG from Astro template
├── dags/output/ # Output folder (CSV files)
├── tests/ # DAG tests
├── requirements.txt # Python dependencies
├── Dockerfile # Docker container definition
├── packages.txt # System-level dependencies
├── airflow_settings.yaml # Airflow variables & settings
└── README.md # Project documentation

yaml
Kopiuj
Edytuj

---

## 🚀 Run Locally
1. Install **[Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli)**  
2. Start Airflow with Docker:
   ```bash
   astro dev start
Open the Airflow UI:
👉 http://localhost:8080
Username: admin
Password: admin

Trigger the DAG weather_etl and check the output file at:

bash
Kopiuj
Edytuj
dags/output/weather.csv
🛠️ Tech Stack
Apache Airflow – workflow orchestration

Python – ETL logic

Open-Meteo API – weather data source

Docker + Astro CLI – local runtime environment

👩‍💻 Author
Project created as part of learning ETL pipelines with Airflow – Ola Barczyk

yaml
Kopiuj
Edytuj

---
