from azure.identity import DeviceCodeCredential
from msgraph import GraphServiceClient
import asyncio

async def main():
    tenant_id = ""
    client_id = ""

    GRAPH_SCOPES = ["User.Read"]

    credential = DeviceCodeCredential(
        tenant_id=tenant_id,
        client_id=client_id,
    )

    # Create a Microsoft Graph client.
    graph_client = GraphServiceClient(
        credential,
        GRAPH_SCOPES,
    )

    user = await graph_client.me.get()

    if user:
            print("Microsoft Graph call completed successfully")
            print(f"Display name: {user.display_name}")
            print(f"User principal name: {user.user_principal_name}")
            print(f"User ID: {user.id}")
    credential.close()

if __name__ == "__main__":
    asyncio.run(main())