#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm


base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = f'{base_url}yellow_tripdata_2021-07.csv.gz'

pg_user = 'root'
pg_pass = 'root'
pg_host = 'localhost'
pg_port = 5432
pg_db = 'taxis'

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


df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[20]:


engine = create_engine('postgresql://root:root@localhost:5432/taxis')


# In[22]:


print(pd.io.sql.get_schema(
    df,
    name='yellow_taxi',
    con=engine,
))


df.head(0).to_sql(
    name='yellow_taxi',
    con=engine,
    if_exists='replace',
    )


df_iter = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000
)





for chunk in tqdm(df_iter):
    chunk.to_sql(
    name='yellow_taxi',
    con=engine,
    if_exists='append',
        )



















