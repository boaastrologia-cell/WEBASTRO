#!/usr/bin/env python
"""
Script de teste para validar instalação do WEBASTRO com Odisseu
Executa uma série de verificações para garantir que tudo está funcionando corretamente
"""

import sys
import os
import subprocess
import json
from pathlib import Path

# Cores para output no terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    """Imprimir cabeçalho"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}\n")

def print_success(text):
    """Imprimir mensagem de sucesso"""
    print(f"{Colors.GREEN}✅ {text}{Colors.RESET}")

def print_error(text):
    """Imprimir mensagem de erro"""
    print(f"{Colors.RED}❌ {text}{Colors.RESET}")

def print_warning(text):
    """Imprimir mensagem de aviso"""
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.RESET}")

def print_info(text):
    """Imprimir informação"""
    print(f"{Colors.BLUE}ℹ️  {text}{Colors.RESET}")

class WebastroTester:
    """Classe para executar testes de instalação"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.passed_tests = 0
        self.failed_tests = 0
        self.warnings = 0
    
    def run_all_tests(self):
        """Executar todos os testes"""
        print_header("🚀 WEBASTRO - Teste de Instalação")
        
        tests = [
            self.test_python_version,
            self.test_directory_structure,
            self.test_dependencies,
            self.test_environment_file,
            self.test_imports,
            self.test_config,
            self.test_odisseu_module,
        ]
        
        for test in tests:
            try:
                test()
            except Exception as e:
                print_error(f"Erro ao executar teste: {e}")
                self.failed_tests += 1
        
        self.print_summary()
    
    def test_python_version(self):
        """Teste 1: Verificar versão do Python"""
        print_info("Teste 1: Verificando versão do Python...")
        
        version = sys.version_info
        if version.major == 3 and version.minor >= 8:
            print_success(f"Python {version.major}.{version.minor}.{version.micro} ✓")
            self.passed_tests += 1
        else:
            print_error(f"Python 3.8+ requerido. Você tem {version.major}.{version.minor}")
            self.failed_tests += 1
    
    def test_directory_structure(self):
        """Teste 2: Verificar estrutura de diretórios"""
        print_info("Teste 2: Verificando estrutura de diretórios...")
        
        required_dirs = [
            'config',
            'src',
            'tests',
        ]
        
        required_files = [
            'README.md',
            'QUICKSTART.md',
            'requirements.txt',
            '.env.example',
            '.gitignore',
            'main.py',
        ]
        
        all_exist = True
        
        for dir_name in required_dirs:
            dir_path = self.project_root / dir_name
            if dir_path.exists() and dir_path.is_dir():
                print_success(f"Diretório '{dir_name}' encontrado")
            else:
                print_error(f"Diretório '{dir_name}' não encontrado")
                all_exist = False
        
        for file_name in required_files:
            file_path = self.project_root / file_name
            if file_path.exists():
                print_success(f"Arquivo '{file_name}' encontrado")
            else:
                print_error(f"Arquivo '{file_name}' não encontrado")
                all_exist = False
        
        if all_exist:
            self.passed_tests += 1
        else:
            self.failed_tests += 1
    
    def test_dependencies(self):
        """Teste 3: Verificar dependências instaladas"""
        print_info("Teste 3: Verificando dependências instaladas...")
        
        required_packages = [
            'flask',
            'dotenv',
            'pytest',
        ]
        
        all_installed = True
        for package in required_packages:
            try:
                __import__(package.replace('-', '_'))
                print_success(f"Pacote '{package}' instalado")
            except ImportError:
                print_warning(f"Pacote '{package}' não encontrado - execute: pip install -r requirements.txt")
                all_installed = False
                self.warnings += 1
        
        if all_installed or self.warnings < 3:
            self.passed_tests += 1
        else:
            self.failed_tests += 1
    
    def test_environment_file(self):
        """Teste 4: Verificar arquivo .env"""
        print_info("Teste 4: Verificando arquivo de ambiente...")
        
        env_file = self.project_root / '.env'
        env_example = self.project_root / '.env.example'
        
        if env_example.exists():
            print_success("Arquivo '.env.example' encontrado")
        else:
            print_error("Arquivo '.env.example' não encontrado")
            self.failed_tests += 1
            return
        
        if env_file.exists():
            print_success("Arquivo '.env' existe")
            self.passed_tests += 1
        else:
            print_warning("Arquivo '.env' não existe - execute: cp .env.example .env")
            self.warnings += 1
            self.passed_tests += 1
    
    def test_imports(self):
        """Teste 5: Verificar imports essenciais"""
        print_info("Teste 5: Verificando imports essenciais...")
        
        try:
            import flask
            print_success("Flask importado com sucesso")
        except ImportError as e:
            print_error(f"Erro ao importar Flask: {e}")
            self.failed_tests += 1
            return
        
        try:
            from dotenv import load_dotenv
            print_success("python-dotenv importado com sucesso")
        except ImportError as e:
            print_error(f"Erro ao importar python-dotenv: {e}")
            self.failed_tests += 1
            return
        
        self.passed_tests += 1
    
    def test_config(self):
        """Teste 6: Verificar configurações"""
        print_info("Teste 6: Verificando arquivo de configurações...")
        
        try:
            # Adicionar projeto ao path
            sys.path.insert(0, str(self.project_root))
            from config.settings import ODISSEU_CONFIG, ENVIRONMENT
            
            print_success("Configurações carregadas com sucesso")
            print_info(f"  - Ambiente: {ENVIRONMENT}")
            print_info(f"  - Endpoint Odisseu: {ODISSEU_CONFIG.get('endpoint')}")
            
            self.passed_tests += 1
        except Exception as e:
            print_error(f"Erro ao carregar configurações: {e}")
            self.failed_tests += 1
    
    def test_odisseu_module(self):
        """Teste 7: Verificar módulo Odisseu"""
        print_info("Teste 7: Verificando módulo de integração Odisseu...")
        
        try:
            sys.path.insert(0, str(self.project_root))
            from src.odisseu_integration import OdisseuAgent, OdisseuError
            
            print_success("Módulo Odisseu importado com sucesso")
            
            # Tentar criar instância
            agent = OdisseuAgent(
                api_key="test_key",
                endpoint="http://localhost:8000"
            )
            
            print_success("Agente Odisseu instanciado com sucesso")
            
            # Testar informações
            info = agent.get_info()
            print_success(f"Agente retorna informações: {info['name']} v{info['version']}")
            
            # Testar processamento de query
            response = agent.process_query("teste")
            if "response" in response:
                print_success("Agente processa queries corretamente")
            
            self.passed_tests += 1
        except Exception as e:
            print_error(f"Erro com módulo Odisseu: {e}")
            self.failed_tests += 1
    
    def print_summary(self):
        """Imprimir resumo dos testes"""
        print_header("📊 Resumo dos Testes")
        
        total = self.passed_tests + self.failed_tests
        percentage = (self.passed_tests / total * 100) if total > 0 else 0
        
        print_success(f"Testes Aprovados: {self.passed_tests}")
        if self.failed_tests > 0:
            print_error(f"Testes Falhados: {self.failed_tests}")
        if self.warnings > 0:
            print_warning(f"Avisos: {self.warnings}")
        
        print(f"\nTaxa de sucesso: {percentage:.1f}%\n")
        
        if self.failed_tests == 0:
            print_success("✨ Todos os testes passaram! WEBASTRO está pronto para usar.")
            print_info("\nPróximos passos:")
            print_info("  1. Configure suas variáveis de ambiente em .env")
            print_info("  2. Execute: python main.py")
            print_info("  3. Acesse: http://localhost:5000/health")
            return 0
        else:
            print_error("⚠️  Alguns testes falharam. Corrija os erros acima.")
            return 1

def main():
    """Função principal"""
    tester = WebastroTester()
    exit_code = tester.run_all_tests()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
