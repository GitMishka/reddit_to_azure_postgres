import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from datetime import datetime
import os

# connect_str = ""
# container_name = ""
# blob_name = ".csv" 

file_repo_path = "C:\\Users\\Misha\\Desktop\\GitHub\\reddit_to_azure_postgres"
original_file_name = "sample.csv"
original_file_path = os.path.join(file_repo_path, original_file_name)

df = pd.read_csv(original_file_path)

current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
new_file_name = f"sample_{current_datetime}.csv"
new_file_path = os.path.join(file_repo_path, new_file_name)

