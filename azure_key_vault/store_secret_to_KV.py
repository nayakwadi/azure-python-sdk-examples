import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.keyvault.secrets import SecretClient

# Authenticate using the Azure Identity library
# In Azure DevOps, this works if you use the Azure CLI or Managed Identity

subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID") 
tenant_id = os.environ.get("AZURE_TENANT_ID")
credential = DefaultAzureCredential()
vault_name ="iac-task-kv"

# Step 1: Use Management SDK to create (or get) a Key Vault
kv_client = KeyVaultManagementClient(credential, subscription_id)

# # Step 2: Use Client SDK to add and retrieve a secret
vault_uri = f"https://{vault_name}.vault.azure.net"
secret_client = SecretClient(vault_url=vault_uri, credential=credential)

print("Storing a secret...")
secret_client.set_secret("azuresqladmin", "<some-password-to-store>")