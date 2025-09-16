import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

class Config:
    KEY = os.getenv('SUBSCRIPTION_KEY')  # A chave do Azure
    CONTENT = os.getenv('ENDPOINT')  # O endpoint do Azure
    AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    CONTAINER_NAME = os.getenv('CONTAINER_NAME')
    STORAGE_ACCOUNT_NAME = os.getenv('STORAGE_ACCOUNT_NAME')