from minio import Minio
from logzero import logger
import io
from extract_customers import get_credentials


def upload_data(json_file, bucket, object, file):
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

	logger.info("File is being uploaded...")

	# Create the bucket if it doesn't exist
	if not client.bucket_exists(bucket):
		client.make_bucket(bucket)
		print(f"Bucket '{bucket}' created successfully.")

	# Upload file to Minio
	client.fput_object(bucket, object, file)
	logger.info("File is now uploaded...")
