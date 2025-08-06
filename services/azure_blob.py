import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
load_dotenv()

AZURE_CONN_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "videos"

def upload_video_to_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONN_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.filename)

    blob_client.upload_blob(file, overwrite=True)
    return blob_client.url
