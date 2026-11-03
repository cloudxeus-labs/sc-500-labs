# SC-500 course code

Code for the Cloudxeus course **SC-500**. Each folder is one section of the course, under the same
name you see in the videos.

| Section |
|---|
| 01. Manage identity, access, and governance |
| 02. Secure storage, databases, and networking |
| 03. Secure compute |

## Before you start

You need:

- Python 3.13
- An Azure subscription
- The [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli), signed in with `az login`
- [Docker](https://docs.docker.com/get-started/get-docker/), to build the container images in section 03
- [kubectl](https://learn.microsoft.com/azure/aks/learn/quick-kubernetes-deploy-cli), for the `kubernetes` folder in section 03 (`az aks install-cli` installs it)

## Run a section

Sections 01 and 03 have their own `requirements.txt`, so give each its own virtual environment. On
Windows:

```powershell
cd "01. Manage identity, access, and governance"
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On macOS or Linux, activate it with `source .venv/bin/activate`.

- The `04_commands` files hold Azure CLI commands to run one at a time, written for Bash. In
  PowerShell, replace each `\` at the end of a line with a backtick (`` ` ``).
- The PDFs are made-up company documents to upload to your own storage account.
- In section 03, `app.py` and `backend.py` are the two containers, built with `Dockerfile` and
  `Dockerfile.backend` and pushed to your own container registry.

## Use your own Azure resources

The videos show the instructor's Azure resources. Here, those names are placeholders in angle
brackets, and blank settings such as `client_secret = ""` are for your own values. Replace them
before you run a file, including the angle brackets:

| Placeholder | Replace with |
|---|---|
| `<your-key-vault>` | Your Key Vault's name |
| `<your-storage-account>` | Your storage account's name |
| `<your-registry>` | Your container registry's name (the part before `.azurecr.io`) |
| `<your-managed-identity>` | Your user-assigned managed identity's name |
| `<your-subscription-id>`, `<your-resource-group>` | Your subscription ID and resource group |
| `<your-entra-group-object-id>` | The object ID of your Microsoft Entra group |
| `tenant_id`, `client_id`, `client_secret` | Your tenant ID, and your app registration's client ID and secret |
| `--account-key ""` | Your storage account's access key |

## Keep your keys safe

**Never commit or share a file with a secret or key in it.** Anyone who gets one can reach your data
or run up charges on your Azure subscription.

- Before you commit or push your own copy, set any secrets and keys back to `""`.
- If one does get out, regenerate it in the Azure portal straight away (a new client secret, or a
  rotated storage key). Deleting the file isn't enough.
- `.env` is already in `.gitignore`. Don't remove it.

## Azure costs

These labs create Azure resources that can cost money while they exist, especially the AKS cluster
and container instances. Delete what you created when you finish, usually by deleting its resource
group.

## License

[MIT](LICENSE). The code is provided as is, as learning material.
