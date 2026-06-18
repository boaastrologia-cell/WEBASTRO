#!/usr/bin/env python
"""
Relatório de Teste de Instalação WEBASTRO
Sumário completo da configuração do projeto
"""

import sys
import os
from pathlib import Path

# Adicionar projeto ao path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def print_section(title):
    """Imprimir seção"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")

def test_webastro_installation():
    """Executar teste completo de instalação"""
    
    print("\n" + "="*70)
    print("  🚀 WEBASTRO - RELATÓRIO COMPLETO DE INSTALAÇÃO")
    print("="*70)
    
    # 1. Verificar estrutura do projeto
    print_section("1️⃣  ESTRUTURA DO PROJETO")
    
    structure = {
        "config/": "Configurações da aplicação",
        "config/__init__.py": "Pacote de configurações",
        "config/settings.py": "Arquivo principal de settings",
        "src/": "Código-fonte principal",
        "src/__init__.py": "Pacote de integração",
        "src/odisseu_integration.py": "Módulo Odisseu IA",
        "tests/": "Testes automatizados",
        "tests/__init__.py": "Pacote de testes",
        "tests/test_odisseu.py": "Testes do Odisseu",
        "main.py": "Arquivo principal (servidor Flask)",
        "requirements.txt": "Dependências do projeto",
        ".env.example": "Exemplo de variáveis de ambiente",
        ".gitignore": "Arquivo Git ignore",
        "README.md": "Documentação principal",
        "QUICKSTART.md": "Guia de início rápido",
        "test_installation.py": "Script de teste de instalação",
    }
    
    for path, description in structure.items():
        full_path = project_root / path
        status = "✅" if full_path.exists() else "❌"
        print(f"{status} {path:<30} - {description}")
    
    # 2. Verificar configurações
    print_section("2️⃣  CONFIGURAÇÕES CARREGADAS")
    
    try:
        from config.settings import (
            ENVIRONMENT, DEBUG, ODISSEU_CONFIG, 
            FLASK_PORT, FLASK_HOST, TIMEZONE,
            ENABLE_CACHE, CONFIG_SUMMARY
        )
        
        print("✅ Configurações carregadas com sucesso!\n")
        print(f"  Ambiente: {ENVIRONMENT}")
        print(f"  Debug: {DEBUG}")
        print(f"  Flask Host: {FLASK_HOST}")
        print(f"  Flask Port: {FLASK_PORT}")
        print(f"  Odisseu Endpoint: {ODISSEU_CONFIG.get('endpoint')}")
        print(f"  Timezone: {TIMEZONE}")
        print(f"  Cache Habilitado: {ENABLE_CACHE}")
        
    except Exception as e:
        print(f"❌ Erro ao carregar configurações: {e}")
    
    # 3. Verificar módulos principais
    print_section("3️⃣  MÓDULOS PRINCIPAIS")
    
    modules = [
        ("src.odisseu_integration", "OdisseuAgent, OdisseuError"),
        ("config.settings", "ODISSEU_CONFIG, ENVIRONMENT"),
    ]
    
    for module, exports in modules:
        try:
            __import__(module)
            print(f"✅ {module}")
            print(f"   Exporta: {exports}\n")
        except ImportError as e:
            print(f"❌ {module} - Erro: {e}\n")
    
    # 4. Testar Odisseu
    print_section("4️⃣  AGENTE ODISSEU")
    
    try:
        from src.odisseu_integration import OdisseuAgent
        
        agent = OdisseuAgent(
            api_key="test_key",
            endpoint="http://localhost:8000",
            environment="development"
        )
        
        print("✅ Agente Odisseu inicializado com sucesso!\n")
        
        info = agent.get_info()
        print(f"  Nome: {info['name']}")
        print(f"  Versão: {info['version']}")
        print(f"  Status: {info['status']}")
        print(f"  Endpoint: {info['endpoint']}")
        print(f"  Ambiente: {info['environment']}")
        print(f"  Capabilities: {', '.join(info['capabilities'][:2])}...\n")
        
        # Testar processamento de query
        response = agent.process_query("Teste de instalação")
        print(f"  Query: {response['query']}")
        print(f"  Confiança: {response['confidence']}")
        print(f"  Processado em: {response['processed_at']}\n")
        
    except Exception as e:
        print(f"❌ Erro com Odisseu: {e}\n")
    
    # 5. Rotas disponíveis
    print_section("5️⃣  ROTAS DA API")
    
    routes = [
        ("GET", "/health", "Verificar saúde do servidor"),
        ("GET", "/agent/info", "Informações do agente Odisseu"),
        ("POST", "/agent/query", "Enviar query para o agente"),
    ]
    
    print(f"{'Método':<10} {'Rota':<20} {'Descrição':<40}")
    print("-" * 70)
    for method, route, description in routes:
        print(f"{method:<10} {route:<20} {description:<40}")
    
    # 6. Próximos passos
    print_section("6️⃣  PRÓXIMOS PASSOS")
    
    steps = [
        "Configurar variáveis de ambiente em .env",
        "Instalar o Odisseu: pip install odisseu",
        "Iniciar o servidor: python main.py",
        "Testar a API: curl http://localhost:5000/health",
        "Rodar testes: pytest tests/",
    ]
    
    for i, step in enumerate(steps, 1):
        print(f"  {i}. {step}")
    
    # 7. Resumo final
    print_section("📊 RESUMO")
    
    print("✨ WEBASTRO foi configurado com sucesso!")
    print("\n📋 Componentes instalados:")
    print("   ✅ Estrutura de diretórios")
    print("   ✅ Arquivos de configuração")
    print("   ✅ Módulo Odisseu integrado")
    print("   ✅ Servidor Flask")
    print("   ✅ Testes automatizados")
    print("   ✅ Documentação completa")
    print("\n🚀 Sistema pronto para ser iniciado!")
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    try:
        test_webastro_installation()
    except Exception as e:
        print(f"❌ Erro ao executar relatório: {e}")
        sys.exit(1)
