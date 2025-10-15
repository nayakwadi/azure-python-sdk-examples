import os
from azure.identity import DefaultAzureCredential, CredentialUnavailableError
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.keyvault.secrets import SecretClient

# Authenticate using the Azure Identity library
# In Azure DevOps, this works if you use the Azure CLI or Managed Identity
credential = DefaultAzureCredential()
subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")  #"5e9e32c1-3ce2-41c4-958f-82dcdfb98924"

# Step 1: Use Management SDK to create (or get) a Key Vault
kv_client = KeyVaultManagementClient(credential, subscription_id)

resource_group = "linuxvm-rg"
vault_name = "iac-task-kv"
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