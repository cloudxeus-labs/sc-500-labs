# pip install msgraph-sdk
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
import asyncio

async def main():
    tenant_id = ""
    client_id = ""
    client_secret = ""

    credential = ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret,
    )

    graph_client = GraphServiceClient(credential)

    users_page = await graph_client.users.get()

    if users_page and users_page.value:
            for user in users_page.value[:10]:
                print(f"Name: {user.display_name}")
                print(f"User principal name: {user.user_principal_name}")
                print(f"User ID: {user.id}")
                print("-" * 40)

    await credential.close()

if __name__ == "__main__":
    asyncio.run(main())