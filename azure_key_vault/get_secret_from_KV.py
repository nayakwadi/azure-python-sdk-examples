import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.keyvault.secrets import SecretClient

# Authenticate using the Azure Identity library
# In Azure DevOps, this works if you use the Azure CLI or Managed Identity

#Below works in local VS code, ensure to provide environment variables
#subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID") 
#tenant_id = os.environ.get("AZURE_TENANT_ID")


credential = DefaultAzureCredential()
vault_name ="iac-task-kv"


# Use Client SDK to retrieve a secret
vault_uri = f"https://{vault_name}.vault.azure.net"
secret_client = SecretClient(vault_url=vault_uri, credential=credential)

print("Retrieving a secret...")
secret_obtained=secret_client.get_secret("azuresqladmin")
print(secret_obtained)
print(secret_obtained.value)
