import pandas as pd
from azure.storage.blob import BlobServiceClient
from datetime import datetime
import os
import config

connect_str = config.github1
container_name = "github1"

file_repo_path = "C:\\Users\\Misha\\Desktop\\GitHub\\reddit_to_azure_postgres"
original_file_name = "sample.csv"
original_file_path = os.path.join(file_repo_path, original_file_name)

df = pd.read_csv(original_file_path)

current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
new_file_name = f"data_{current_datetime}.csv"
new_file_path = os.path.join(file_repo_path, new_file_name)

df.to_csv(new_file_path, index=False)

blob_name = new_file_name

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

with open(new_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"The file '{new_file_name}' has been uploaded to Azure Blob Storage.")
