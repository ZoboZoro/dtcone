#!/usr/bin/env python
# coding: utf-8

import logging
import pandas as pd
from tqdm.auto import tqdm

from config import dtype, engine, parse_dates, file_path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s - %(levelname)s',
    filename='logs/ingestion.log'
    
)

def ingest_parquet(
        file: str,
        # dtype: dict,
        # parse_dates: list,
        engine,
        chunksize=100000,
):

    """
    Function to ingest data to postgres
    """

    df = pd.read_parquet(
        file,
        dtype=dtype,
        parse_dates=parse_dates,
    )


    # Creates empty table in db
    df.head(0).to_sql(
        name='green_taxi',
        con=engine,
        if_exists='replace',
        )


    # Batch load into database
    df.to_sql(
        name='yellow_taxi',
        con=engine,
        if_exists='append',
        )
    logging.info(f'writing records of {len(df)}')


def ingest_csv(
        file: str,
        dtype: dict,
        parse_dates: list,
        engine,
        chunksize=100000,
):

    """
    Function to ingest csv data to postgres
    """

    df = pd.read_parquet(
        file,
        dtype=dtype,
        parse_dates=parse_dates,
    )


    # Creates empty table in db
    df.head(0).to_sql(
        name='yellow_taxi',
        con=engine,
        if_exists='replace',
        )

    # Creates df iterator
    df_iter = pd.read_(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize
    )

    # Batch load into database
    for chunk in tqdm(df_iter):
        chunk.to_sql(
            name='yellow_taxi',
            con=engine,
            if_exists='append',
            )
        logging.info(f'writing records of {len(chunk)}')

if __name__ == '__main__':
    ingest(url, dtype, parse_dates, engine)
