import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.keyvault.secrets import SecretClient

# Authenticate using the Azure Identity library
# In Azure DevOps, this works if you use the Azure CLI or Managed Identity

#subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID") 
#tenant_id = os.environ.get("AZURE_TENAT_ID")
credential = DefaultAzureCredential()
vault_name ="iac-task-kv"

# Step 1: Use Management SDK to create (or get) a Key Vault
#kv_client = KeyVaultManagementClient(credential, subscription_id)
kv_client = KeyVaultManagementClient("1830154f-384b-4c58-a89e-002e8867da1c", "5e9e32c1-3ce2-41c4-958f-82dcdfb98924")

# # Step 2: Use Client SDK to add and retrieve a secret
vault_uri = f"https://{vault_name}.vault.azure.net"
secret_client = SecretClient(vault_url=vault_uri, credential=credential)

print("Retrieving a secret...")
secret_obtained=secret_client.get_secret("azuresqladmin")
print(secret_obtained)
print(secret_obtained.value)
