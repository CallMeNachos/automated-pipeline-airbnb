import requests

import json
import pandas as pd
from collections.abc import Iterator
from requests.exceptions import ConnectionError


def fetch_total_records(url: str) -> int:
	response = requests.get(url + f"/records?offset={1}").text
	total_records = int(json.loads(response)["total_count"])
	return total_records


def fetch_records(url: str, offset: int) -> Iterator[dict]:
	i = 0
	while i < offset:
		url_page = url + f"/records?where=column_19%3D%22France%22&offset={i}"
		try:
			response = requests.get(url_page).text
		except ConnectionError as e:
			print(f"URL {url_page} is wrong")

		result = json.loads(response)['results']
		print(f"rows processed: {i}/{offset}")
		yield result[0]
		i += 1


def create_dataframe(url: str, offset) -> pd.DataFrame:
	"""
	Collect records in a Pandas Dataframe
	"""
	df = pd.DataFrame()
	for i, record in enumerate(fetch_records(url, offset)):
		new_record = pd.json_normalize(record)
		df = pd.concat([df, new_record])
		df = df.reset_index()
		df = df.rename(
			columns={
				'coordinates.lon': 'lon',
				'coordinates.lat': 'lat'})
	return df

