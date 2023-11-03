import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from datetime import datetime
import os

# connect_str = ""
# container_name = ""
# blob_name = ".csv" 

file_path = "sample.csv"
updated_file_path = "path_to_your_local_sample_with_datetime.csv"