import requests
from constants import URL
import json
import pandas as pd
from collections.abc import Iterator
from typing import Optional


def fetch_total_records(url: str) -> int:
    response = requests.get(url + f"/records?offset={1}").text
    total_records = int(json.loads(response)["total_count"])
    return total_records


def fetch_records(url: str, total_records: int) -> Iterator[dict]:
    for i in range(0, total_records):
        url_page = url + f"/records?offset={i}"
        response = requests.get(url_page).text
        result = json.loads(response)['results']
        yield result[0]


def to_dataframe(records: Iterator[dict]) -> pd.DataFrame:
    """
    Collect records in a Pandas Dataframe
    """
    df = pd.DataFrame()
    for i, record in enumerate(records):
        new_record = pd.json_normalize(record)
        print(new_record)
        df = pd.concat([df, new_record])
    return df


if __name__ == '__main__':
    total_records = 5
    pd.set_option('display.max_columns', 30)
    print(to_dataframe(fetch_records(URL, total_records)))
