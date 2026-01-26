
from sqlalchemy import create_engine

pg_user = 'root'
pg_pass = 'root'
pg_host = 'localhost'
pg_port = 5432
pg_db = 'taxis'

engine = create_engine(
        f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
        )

base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/' \
            'releases/download/yellow/'
url = f'{base_url}yellow_tripdata_2021-07.csv.gz'

dtype = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "string",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64",
    }

parse_dates = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime"
    ]
