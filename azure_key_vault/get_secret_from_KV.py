import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.keyvault.secrets import SecretClient


credential = DefaultAzureCredential()
vault_name ="iac-task-kv"


# # Step 2: Use Client SDK to add and retrieve a secret
vault_uri = f"https://{vault_name}.vault.azure.net"
secret_client = SecretClient(vault_url=vault_uri, credential=credential)

print("Retrieving a secret...")
secret_obtained=secret_client.get_secret("azuresqladmin")
print(secret_obtained)
print(secret_obtained.value)
