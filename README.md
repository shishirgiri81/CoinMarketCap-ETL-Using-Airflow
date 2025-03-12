Got it! Here is the updated `README.md` file assuming the project is complete and the data is successfully loaded into the database.

---

# CoinMarketCap ETL Pipeline with Airflow

## Project Overview

This project implements an **ETL pipeline** using **Apache Airflow** to fetch cryptocurrency data from the **CoinMarketCap API**, process it, and load it into a **database**. The pipeline fetches the latest data, transforms it into a structured format, and stores the processed data in a database for further analysis.

### Features:
- **Extraction**: Fetches cryptocurrency data from the CoinMarketCap API.
- **Transformation**: Processes and normalizes the JSON data into a structured format using **Pandas**.
- **Loading**: Loads the transformed data into a database (e.g., MySQL, PostgreSQL).
- **Orchestration**: The entire process is orchestrated using **Apache Airflow**, which automates the scheduling and execution of tasks.

### Data Flow:
1. **Extract**: Data is fetched from the CoinMarketCap API and saved as a JSON file.
2. **Transform**: The JSON data is transformed into a structured format using Pandas.
3. **Load**: The transformed data is loaded into a database for storage and further analysis.

The pipeline is designed to run **daily**, but the frequency can be adjusted by modifying the DAG's schedule.

## Requirements

Before running this project, make sure you have the following installed:

- **Python 3.8+**
- **Apache Airflow 2.x**
- **requests**
- **pandas**
- **SQLAlchemy** (for database connection)
- **psycopg2** or **mysql-connector-python** (for PostgreSQL/MySQL connection)

You can install the dependencies using `pip`:

```bash
pip install apache-airflow requests pandas sqlalchemy psycopg2
```

## Setup

### 1. **Set up Apache Airflow**

To set up Apache Airflow, follow the [official Airflow setup guide](https://airflow.apache.org/docs/apache-airflow/stable/start/index.html). Once installed, start the Airflow services:

```bash
airflow db init
airflow webserver --port 8080
```

The Airflow UI will be available at `http://localhost:8080`.

### 2. **API Key for CoinMarketCap**

You need a **CoinMarketCap API key** to access the cryptocurrency data. To obtain an API key:

1. Visit [CoinMarketCap API](https://coinmarketcap.com/api/) and sign up for an API key.
2. Replace the value of `X-CMC_PRO_API_KEY` in the `extract()` function in `main.py` with your API key:

```python
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'your-api-key-here',  # Replace with your API key
}
```

### 3. **Database Setup**

1. **Create a database** (e.g., PostgreSQL or MySQL).
2. Modify the database connection settings in the Airflow configuration or directly in the DAG file (`main.py`) to connect to your database.
   
For PostgreSQL, the connection string can be set in the Airflow UI under **Admin** > **Connections** or in the `main.py` as:

```python
from sqlalchemy import create_engine

# Example for PostgreSQL
engine = create_engine('postgresql://user:password@localhost:5432/crypto_db')

# Or for MySQL
# engine = create_engine('mysql+mysqlconnector://user:password@localhost/crypto_db')
```

Make sure your Airflow environment has access to the database.

### 4. **Directory Structure**

This is the expected directory structure for your project:

```
coinmarketcap-etl/
├── airflow_project/
│   ├── dags/
│   │   └── main.py      # Your main Airflow DAG file
│   ├── data/
│   │   └── crypto_data.json    # The output JSON file for processed data
└── README.md
```

### 5. **Run the Pipeline**

To start the pipeline:

1. Place the `main.py` file under the `dags/` folder in your Airflow home directory.
2. Start the Airflow scheduler:
   ```bash
   airflow scheduler
   ```
3. You can now trigger the DAG from the Airflow UI or wait for it to run according to the defined schedule (`@daily`).

### 6. **Task Workflow**

The pipeline is composed of two tasks:
- **`extract`**: Fetches data from CoinMarketCap and saves it as a JSON file.
- **`transform`**: Processes the raw JSON data, normalizes it, and saves the cleaned data back into the same file.
- **`load`** (Completed): The transformed data is loaded into a database.

### 7. **Database Schema**

After the data is successfully loaded into the database, the schema will look something like this:

- **id**: The unique identifier for the cryptocurrency.
- **name**: The name of the cryptocurrency.
- **symbol**: The symbol of the cryptocurrency (e.g., BTC for Bitcoin).
- **slug**: The slug used for the cryptocurrency.
- **date_added**: The date the cryptocurrency was added.
- **max_supply**: The maximum supply of the cryptocurrency.
- **circulating_supply**: The current circulating supply.
- **total_supply**: The total supply of the cryptocurrency.
- **cmc_rank**: The CoinMarketCap ranking.
- **last_updated**: The last updated timestamp for the data.
- **price**: The price in USD.
- **volume_24h**: The 24-hour trading volume in USD.
- **percent_change_1h**: The percent change in price in the last hour.
- **percent_change_24h**: The percent change in price in the last 24 hours.
- **percent_change_7d**: The percent change in price in the last 7 days.
- **market_cap**: The market cap in USD.
- **market_cap_dominance**: The market cap dominance in the market.

## Troubleshooting

- **Invalid API Key**: Ensure that you have replaced the API key in the `main.py` file with your own.
- **Data Issues**: Check the JSON file after extraction to ensure the data is properly fetched from the API.
- **Database Connection**: Ensure that the database connection is configured properly and accessible from the Airflow environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This updated README reflects that the project is complete, with the final step being the loading of data into a database. Let me know if you need further adjustments!
