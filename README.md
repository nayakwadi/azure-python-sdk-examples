This repo contains sample scripts to connect to Azure Subscription & perform operations on  Azure Resources

**Prerequisites:
1. create a project folder
2. Inside the project folder, create a python virtual environment. We need this step as we would download various azure packages in this environment
3. Commands to execute
    a. pip3 install --upgrade pip
    b. pip3 install azure-storage-blob azure-identity azure-key-vault
4. Create a storage account in Azure Portal. Ensure the ananonymous access enabled for storage account as it would be easy to test the commands from local machine
5. Go to Storage Browser -->Blob Containers-->Add a Container. Add some dummy file inside this container
6. Add "Storage Blob Data Contributor" role to the account which would be used in local machine
7. From local machine, open a terminal and login to azure using az cli commands and select the appropriate subscriptions
8. DefaultCredentials() used in scripts would need the az login to be run upfront.


