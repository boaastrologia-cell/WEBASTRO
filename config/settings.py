"""
Configurações da aplicação WEBASTRO com Odisseu
"""

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações Gerais
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Configurações Odisseu
ODISSEU_CONFIG = {
    "api_key": os.getenv("ODISSEU_API_KEY"),
    "endpoint": os.getenv("ODISSEU_ENDPOINT", "http://localhost:8000"),
    "timeout": int(os.getenv("ODISSEU_TIMEOUT", 30)),
    "environment": ENVIRONMENT,
}

# Configurações Flask
FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_DEBUG = os.getenv("FLASK_DEBUG", DEBUG)

# Configurações de Banco de Dados
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///webastro.db")
DATABASE_POOL_SIZE = int(os.getenv("DATABASE_POOL_SIZE", 10))

# Configurações de Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/webastro.log")

# Configurações de Astronomia
TIMEZONE = os.getenv("TIMEZONE", "America/Sao_Paulo")
LATITUDE = float(os.getenv("LATITUDE", "-15.8267"))
LONGITUDE = float(os.getenv("LONGITUDE", "-47.8822"))

# Configurações de Segurança
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
JWT_SECRET = os.getenv("JWT_SECRET", "dev-jwt-secret-change-in-production")

# Configurações de Cache
ENABLE_CACHE = os.getenv("ENABLE_CACHE", "True").lower() == "true"
CACHE_TTL = int(os.getenv("CACHE_TTL", 3600))

# Configurações de API Keys Externas
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
NASA_API_KEY = os.getenv("NASA_API_KEY", "")

# Validações
if ENVIRONMENT == "production":
    if not os.getenv("ODISSEU_API_KEY"):
        raise ValueError("❌ ODISSEU_API_KEY é obrigatória em produção")
    if SECRET_KEY == "dev-secret-key-change-in-production":
        raise ValueError("❌ SECRET_KEY deve ser alterada em produção")
    if JWT_SECRET == "dev-jwt-secret-change-in-production":
        raise ValueError("❌ JWT_SECRET deve ser alterado em produção")

# Criar diretório de logs se não existir
os.makedirs(os.path.dirname(LOG_FILE) if os.path.dirname(LOG_FILE) else ".", exist_ok=True)

# Configuração de exemplo para exibição
CONFIG_SUMMARY = {
    "environment": ENVIRONMENT,
    "debug": DEBUG,
    "flask_host": FLASK_HOST,
    "flask_port": FLASK_PORT,
    "odisseu_endpoint": ODISSEU_CONFIG["endpoint"],
    "timezone": TIMEZONE,
    "cache_enabled": ENABLE_CACHE,
}
