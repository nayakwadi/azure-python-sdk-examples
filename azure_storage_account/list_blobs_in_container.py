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
    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)
except Exception as ex:
    print('Exception:')
    print(ex)