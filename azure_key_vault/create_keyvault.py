import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient


# Authenticate using the Azure Identity library
#Below works in local VS code, ensure to provide environment variables
#subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID") 
#tenant_id = os.environ.get("AZURE_TENANT_ID")

credential = DefaultAzureCredential()
subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")

# Step 1: Use Management SDK to create (or get) a Key Vault
kv_client = KeyVaultManagementClient(credential, subscription_id)

resource_group = "<rg-name>"
vault_name = "<key-vault-name>"
location = "eastus2"

# Check if the Key Vault already exists
try:
    vault = kv_client.vaults.get(resource_group, vault_name)
    print(f"Key Vault '{vault_name}' already exists.")
except:
    print(f"Creating Key Vault '{vault_name}' ...")
    vault_params = {
        "location": location,
        "properties": {
            "tenant_id": os.environ.get("AZURE_TENANT_ID"),  # extract tenant id
            "sku": {"family": "A", "name": "standard"},
            "access_policies": []  # You can add access policies here
        }
    }
    vault = kv_client.vaults.begin_create_or_update(resource_group, vault_name, vault_params).result()
    print(f"Created Key Vault: {vault.name}")