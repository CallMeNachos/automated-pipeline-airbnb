import json
import os
import pandas as pd
from minio import Minio
from logzero import logger


def get_credentials(json_file):
	"""
	Get MinIO credentials from ./user_credentials.json
	NB: Create your credentials from MinIO localhost before running the module
	:return: Minio credentials
	"""
	abspath = os.path.dirname(os.path.abspath(__file__))
	file = abspath + json_file

	with open(file, 'r') as f:
		credentials = json.load(f)

	# Get localhost id
	localhost_id = credentials["url"].split(":")[-1]

	return credentials["accessKey"], credentials["secretKey"], localhost_id


def customer_data(json_file, bucket: str) -> pd.DataFrame:
	"""
	Retrieve customer data and store in a Pandas DataFrame
	:param json_file: credentials json created in MiniIO
	:param bucket: bucket name in MiniIO
	:return: df
	"""
	# Create a client with the MinIO server playground, its access key and secret key.
	access_key, secret_key, localhost_id = get_credentials(json_file)

	try:
		client = Minio(
			f"localhost:{localhost_id}",
			access_key=access_key,
			secret_key=secret_key,
			secure=False
			)
	except ConnectionError as e:
		logger.error("Can't connect to Minio")

	df = pd.DataFrame()
	if client.bucket_exists(bucket):
		logger.info(f"Connexion to bucket: {bucket}")

		# Get data of an object
		objects = client.list_objects(bucket, prefix='20', recursive=True)

		for obj in objects:
			try:
				response = client.get_object(bucket, obj.object_name)
				# Convert into DataFrame
				result = pd.read_csv(response)
			finally:
				response.close()
				response.release_conn()

			df = pd.concat([df, result])

	else:
		logger.error(f"Bucket [{bucket}] does not exist!")

	logger.info(f"customer data is now loaded")
	return df
