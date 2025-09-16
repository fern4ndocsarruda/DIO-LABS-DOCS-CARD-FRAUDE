from dotenv import load_dotenv
import os
import sys

# Para garantir que o caminho relativo seja correto
print("Current working directory:", os.getcwd())

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()  # O arquivo .env deve estar no mesmo diretório que o script

# Verificar se as variáveis de ambiente estão sendo carregadas corretamente
print("ENDPOINT:", os.getenv("ENDPOINT"))
print("SUBSCRIPTION_KEY:", os.getenv("SUBSCRIPTION_KEY"))
print("AZURE_STORAGE_CONNECTION_STRING:", os.getenv("AZURE_STORAGE_CONNECTION_STRING"))
print("CONTAINER_NAME:", os.getenv("CONTAINER_NAME"))
print("STORAGE_ACCOUNT_NAME:", os.getenv("STORAGE_ACCOUNT_NAME"))
