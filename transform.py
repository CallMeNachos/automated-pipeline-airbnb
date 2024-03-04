import pandas as pd
# from pandasql import sqldf
import pandasql as psql
from logzero import logger


def merge_tables(left_table: str, right_table: str, left_key: str, right_key: str, columns: dict[str]) -> str:
	i = 0
	typo = ", \n"
	select = ""
	for key, val in columns.items():

		if len(val) == 0:
			val = key
		if i == len(columns) - 1:
			typo = ""
		i += 1
		select += f"{key} AS {val}" + typo

	query = f'''
		SELECT 
			{select}
		FROM 
			{left_table} AS left
		LEFT JOIN
			{right_table} AS right
		ON 
			left.{left_key} = right.{right_key}
	'''
	logger.info("Tables are currently merging")
	return query


def aggregated_table(table: str) -> str:
	query = f'''
		SELECT 
			id,
			host_id,
			neighbourhood,
			city,
			country,
			room_price / minimum_nights AS room_price_by_night,
			ROUND(AVG(room_price) OVER (PARTITION BY neighbourhood), 2) AS avg_room_price_neighbourhood,
			ROUND(AVG(room_price) OVER (PARTITION BY city), 2) AS avg_room_price_city,
			ROUND(AVG(room_price) OVER (PARTITION BY country), 2) AS avg_room_price_country,
			COUNT(*) OVER (PARTITION BY neighbourhood) AS nb_host_neighbourhood,
			COUNT(*) OVER (PARTITION BY city) AS nb_host_city,
			COUNT(*) OVER (PARTITION BY country) AS nb_host_country
		FROM
			{table}
	'''
	logger.info("Aggregation are currently running")
	return query
