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
    upload_file_path = os.path.join(local_path, local_file_name)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
    # Upload the local file
    with open(file=upload_file_path, mode="rb") as data:
        blob_client.upload_blob(data)

except Exception as ex:
    print('Exception:')
    print(ex)