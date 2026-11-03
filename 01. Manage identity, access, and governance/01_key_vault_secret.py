from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

key_vault_url="https://<your-key-vault>.vault.azure.net/"
secret_name="dbpassword"

tenant_id=""
client_id=""
client_secret=""

credential=ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

secret_client=SecretClient(
    vault_url=key_vault_url,
    credential=credential
)

secret=secret_client.get_secret(secret_name)

print("Secret retrieved successfully")
print(f"Secret value: {secret.value}")