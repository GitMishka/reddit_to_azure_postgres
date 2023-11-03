import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from datetime import datetime
import os

# connect_str = ""
# container_name = ""
# blob_name = ".csv" 

file_repo_path = "C:\\Users\\Misha\\Desktop\\GitHub\\reddit_to_azure_postgres"
file_name = "sample.csv"
file_path = os.path.join(file_repo_path, file_name)

df = pd.read_csv(file_path)

df