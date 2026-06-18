#!/usr/bin/env python
"""
WEBASTRO - Integração Odisseu com Funcionalidades Astronômicas
Arquivo principal para inicializar e rodar o agente IA Odisseu
"""

import os
import sys
import logging
from dotenv import load_dotenv
from flask import Flask, jsonify

# Carregar variáveis de ambiente
load_dotenv()

# Configurar logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Criar aplicação Flask
app = Flask(__name__)
app.config["DEBUG"] = os.getenv("FLASK_DEBUG", False)

# Importar configurações
try:
    from config.settings import ODISSEU_CONFIG
    logger.info("✅ Configurações carregadas com sucesso")
except Exception as e:
    logger.error(f"❌ Erro ao carregar configurações: {e}")
    sys.exit(1)

# Importar integração Odisseu
try:
    from src.odisseu_integration import OdisseuAgent
    logger.info("✅ Módulo Odisseu importado com sucesso")
except ImportError as e:
    logger.error(f"❌ Erro ao importar Odisseu: {e}")
    logger.warning("⚠️ Certifique-se de que o Odisseu está instalado: pip install odisseu")
    sys.exit(1)


# Inicializar agente Odisseu
try:
    odisseu_agent = OdisseuAgent(**ODISSEU_CONFIG)
    logger.info("✅ Agente Odisseu inicializado com sucesso")
except Exception as e:
    logger.error(f"❌ Erro ao inicializar Odisseu: {e}")
    sys.exit(1)


# Rotas da API
@app.route("/health", methods=["GET"])
def health():
    """Endpoint de health check"""
    return jsonify({
        "status": "ok",
        "message": "WEBASTRO com Odisseu ativo",
        "version": "1.0.0"
    }), 200


@app.route("/agent/info", methods=["GET"])
def agent_info():
    """Retornar informações do agente Odisseu"""
    try:
        info = odisseu_agent.get_info()
        return jsonify({"status": "success", "data": info}), 200
    except Exception as e:
        logger.error(f"Erro ao obter informações do agente: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/agent/query", methods=["POST"])
def agent_query():
    """Enviar query para o agente Odisseu"""
    from flask import request
    
    try:
        data = request.get_json()
        query = data.get("query", "")
        
        if not query:
            return jsonify({"status": "error", "message": "Query não fornecida"}), 400
        
        response = odisseu_agent.process_query(query)
        return jsonify({"status": "success", "data": response}), 200
    except Exception as e:
        logger.error(f"Erro ao processar query: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """Handler para rotas não encontradas"""
    return jsonify({"status": "error", "message": "Rota não encontrada"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handler para erros internos"""
    return jsonify({"status": "error", "message": "Erro interno do servidor"}), 500


def main():
    """Função principal"""
    logger.info("=" * 60)
    logger.info("🚀 WEBASTRO - Iniciando com Odisseu IA")
    logger.info("=" * 60)
    
    port = int(os.getenv("FLASK_PORT", 5000))
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    
    logger.info(f"🌐 Servidor rodando em http://{host}:{port}")
    logger.info(f"📊 Modo DEBUG: {os.getenv('FLASK_DEBUG', False)}")
    logger.info("=" * 60)
    
    app.run(host=host, port=port, debug=os.getenv("FLASK_DEBUG", False))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\n⛔ Servidor interrompido pelo usuário")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Erro fatal: {e}")
        sys.exit(1)
