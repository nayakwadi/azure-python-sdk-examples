import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

account_url = "https://<storageaccount>.blob.core.windows.net"
default_credential = DefaultAzureCredential()

container_name ="samplecontainer"
# Create the BlobServiceClient object
blob_service_client = BlobServiceClient(account_url, credential=default_credential)
# Create the container_client
container_client = blob_service_client.get_container_client("samplecontainer")

try:
    print("Azure Blob Storage Python quickstart sample")

    local_path="<local_file_path>"
    local_file_name="<file_name>"
    
    # Download the blob to a local file
    # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
    download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt')) 
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(file=download_file_path, mode="wb") as download_file:
        download_file.write(container_client.download_blob('<blob_nam_in_container>').readall())

except Exception as ex:
    print('Exception:')
    print(ex)