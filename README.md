# WEBASTRO

Projeto de integração do agente de IA **Odisseu** com funcionalidades astronômicas e web.

## 📋 Pré-requisitos

- Python 3.8+ (ou a versão especificada pelo Odisseu)
- pip (gerenciador de pacotes Python)
- Git
- Variáveis de ambiente configuradas

## 🔧 Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/boaastrologia-cell/WEBASTRO.git
cd WEBASTRO
```

### 2. Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
```bash
cp .env.example .env
# Edite .env com suas configurações
```

### 5. Instalar Odisseu
```bash
# Se Odisseu está no PyPI:
pip install odisseu

# Se é um repositório local:
pip install -e ./odisseu

# Se é um repositório remoto:
pip install git+https://github.com/seu-user/odisseu.git
```

## 🧪 Testando a Instalação

### Teste básico
```bash
python -c "import odisseu; print(odisseu.__version__)"
```

### Rodar testes automatizados
```bash
pytest tests/
```

### Executar o agente
```bash
python main.py
```

### Testar via API (se disponível)
```bash
curl http://localhost:5000/health
```

## 📁 Estrutura do Projeto
```
WEBASTRO/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── main.py
├── tests/
│   └── test_odisseu.py
├── src/
│   └── odisseu_integration.py
└── config/
    └── settings.py
```

## 🐛 Solução de Problemas

**Erro: `ModuleNotFoundError: No module named 'odisseu'`**
- Verifique se o ambiente virtual está ativado
- Reinstale as dependências: `pip install -r requirements.txt`

**Erro ao conectar com Odisseu**
- Verifique as variáveis de ambiente em `.env`
- Consulte a documentação do Odisseu

## 📚 Referências
- [Documentação do Odisseu](#)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

## 👤 Autor
boaastrologia-cell

## 📝 Licença
(Especificar conforme necessário)
