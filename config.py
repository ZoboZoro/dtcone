
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

file_path = './data/green_tripdata_2025-11.parquet'
lookup_path = './data/taxi_zone_lookup.csv'

dtype = {
        "LocationID": "Int64",
        "Borough": "string",
        "Zone": "string",
        "service_zone": "string",
    }
