# GUIA DE INÍCIO RÁPIDO - WEBASTRO com Odisseu

## 🚀 Instalação Rápida

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/boaastrologia-cell/WEBASTRO.git
cd WEBASTRO
```

### 2️⃣ Criar e ativar ambiente virtual
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Configurar ambiente
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

### 5️⃣ Instalar Odisseu (se necessário)
```bash
# Opção 1: PyPI (se disponível)
pip install odisseu

# Opção 2: GitHub
pip install git+https://github.com/seu-usuario/odisseu.git

# Opção 3: Localmente
pip install -e ./odisseu
```

## 🧪 Testando a Instalação

### Teste 1: Verificar importação do Odisseu
```bash
python -c "import src.odisseu_integration; print('✅ Odisseu integrado com sucesso!')"
```

### Teste 2: Verificar configurações
```bash
python -c "from config.settings import CONFIG_SUMMARY; print(CONFIG_SUMMARY)"
```

### Teste 3: Executar testes automatizados
```bash
pytest tests/ -v
```

### Teste 4: Rodar o servidor
```bash
python main.py
```

O servidor estará disponível em `http://localhost:5000`

## 🌐 Testando a API

### Health Check
```bash
curl http://localhost:5000/health
```

Resposta esperada:
```json
{
  "status": "ok",
  "message": "WEBASTRO com Odisseu ativo",
  "version": "1.0.0"
}
```

### Informações do Agente
```bash
curl http://localhost:5000/agent/info
```

Resposta esperada:
```json
{
  "status": "success",
  "data": {
    "name": "Odisseu IA Agent",
    "version": "1.0.0",
    "status": "initialized",
    "endpoint": "http://localhost:8000",
    "environment": "development",
    "capabilities": [
      "natural_language_processing",
      "question_answering",
      "task_automation",
      "astronomy_integration"
    ]
  }
}
```

### Enviar Query para o Agente
```bash
curl -X POST http://localhost:5000/agent/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Olá, como você funciona?"}'
```

Resposta esperada:
```json
{
  "status": "success",
  "data": {
    "query": "Olá, como você funciona?",
    "response": "Sou um agente IA integrado com WEBASTRO. Posso responder perguntas, automatizar tarefas e fornecer informações astronômicas.",
    "confidence": 0.95,
    "processed_at": "2026-06-18T21:05:00.000000"
  }
}
```

## 📊 Estrutura de Diretórios

```
WEBASTRO/
├── main.py                      # Arquivo principal (servidor Flask)
├── requirements.txt             # Dependências do projeto
├── .env.example                 # Exemplo de variáveis de ambiente
├── .gitignore                   # Arquivos ignorados pelo Git
├── README.md                    # Documentação principal
├── QUICKSTART.md               # Este arquivo
│
├── config/
│   └── settings.py              # Configurações da aplicação
│
├── src/
│   └── odisseu_integration.py   # Módulo de integração Odisseu
│
└── tests/
    └── test_odisseu.py          # Testes unitários
```

## 🐛 Solução de Problemas

### Erro: `ModuleNotFoundError: No module named 'odisseu'`
**Solução:**
```bash
# Verifique se o ambiente virtual está ativado
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows

# Reinstale as dependências
pip install -r requirements.txt
```

### Erro: `Port 5000 is already in use`
**Solução:**
```bash
# Opção 1: Alterar porta no .env
# Edite: FLASK_PORT=5001

# Opção 2: Encontrar e matar processo
lsof -i :5000
kill -9 <PID>
```

### Erro: `Cannot import config.settings`
**Solução:**
```bash
# Certifique-se de estar no diretório raiz do projeto
cd WEBASTRO

# Verifique a estrutura dos diretórios
ls -la config/
ls -la src/
```

## 📚 Referências Úteis

- [Documentação Flask](https://flask.palletsprojects.com/)
- [Documentação Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python-dotenv](https://github.com/theskumar/python-dotenv)

## 💡 Próximos Passos

1. ✅ Instalar dependências
2. ✅ Configurar variáveis de ambiente
3. ✅ Rodar testes
4. ✅ Iniciar servidor
5. 📝 Integrar com banco de dados
6. 🔐 Implementar autenticação
7. 📊 Adicionar mais endpoints
8. 🚀 Deploy em produção

## 👥 Suporte

Para dúvidas ou problemas, consulte:
- README.md - Documentação completa
- GitHub Issues - Reporte problemas
- Documentação do Odisseu

---

**Última atualização:** 2026-06-18
