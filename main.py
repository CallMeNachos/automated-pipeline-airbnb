

if __name__ == '__main__':
	import pandasql as psql
	import os
	from logzero import logger
	from constants import URL
	from extract_customers import customer_data
	from extract_api import create_dataframe
	from transform import merge_tables, aggregated_table
	from load import upload_data

	# checking if the directory data exist or not.
	abspath = os.path.dirname(os.path.abspath(__file__))
	if not os.path.exists(abspath + "/data"):
		# if the data directory is not present then create it.
		os.makedirs(abspath + "/data")
		logger.info("/data directory has been created")

	# **************************************************
	#                       Extract
	# **************************************************

	# Retrieve data and create dataframes
	df_customer = customer_data("/user_credentials.json", "companies")
	df_api = create_dataframe(URL, 9990)

	# **************************************************
	#                       Transform
	# **************************************************
	# Apply transformations
	columns = {
		'left.id': 'id',
		'name': '',
		'host_id': '',
		'neighbourhood': '',
		'room_type': '',
		'column_10': 'room_price',
		'minimum_nights': '',
		'number_of_reviews': '',
		'last_review': '',
		'reviews_per_month': '',
		'calculated_host_listings_count': '',
		'availability_365': '',
		'updated_date': '',
		'left.city': 'city',
		'column_19': 'country',
		'column_20': 'location',
		'lon': 'longitude',
		'lat': 'latitude',
		'address': ''
		}

	df_table = psql.sqldf(merge_tables(
		"df_api",
		"df_customer",
		"host_id",
		"id",
		columns
		))

	agg_table = psql.sqldf(aggregated_table("df_table"))

	# **************************************************
	#                       Load
	# **************************************************
	# Convert df to csv files
	customer_file = abspath + "/data/customer_data.csv"
	host_file = abspath + "/data/host_data.csv"

	df_customer.to_csv(customer_file, index=False)
	df_api.to_csv(host_file, index=False)
	agg_table.to_csv(abspath + "/data/agg_table.csv")

	# Upload agg_table in MinIO bucket
	upload_data("/user_credentials.json", "output", "agg_table.csv", abspath + "/data/agg_table.csv")