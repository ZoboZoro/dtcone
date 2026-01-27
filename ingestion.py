#!/usr/bin/env python
# coding: utf-8

import logging
import pandas as pd
from tqdm.auto import tqdm

from config import dtype, engine, file_path, lookup_path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s - %(levelname)s',
    filename='logs/ingestion.log'
    
)

def ingest_parquet(
        file: str,
        table_name: str,
        engine,
):

    """
    Function to ingest data to postgres
    """

    df = pd.read_parquet(
        file,
    )


    # Creates empty table in db
    df.head(0).to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',
        )


    # Load into database
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='append',
        )
    logging.info(f'writing records of {len(df)}')


def ingest_csv(
        file: str,
        dtype: dict,
        parse_dates: list,
        table_name: str,
        engine,
        chunksize=100000,
):

    """
    Function to ingest csv data to postgres
    """

    df = pd.read_csv(
        file,
        dtype=dtype,
        parse_dates=parse_dates,
    )


    # Creates empty table in db
    df.head(0).to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',
        )

    # Creates df iterator
    df_iter = pd.read_csv(
        file,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize
    )

    # Batch load into database
    for chunk in tqdm(df_iter):
        chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists='append',
            )
        logging.info(f'writing records of {len(chunk)}')

if __name__ == '__main__':
    ingest_parquet(file_path, engine, able_name='green_taxi')
    ingest_csv(lookup_path, dtype, engine, table_name='lookup_table')
