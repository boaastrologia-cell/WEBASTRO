"""
Testes unitários para integração Odisseu
"""

import pytest
import sys
import os

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.odisseu_integration import OdisseuAgent, OdisseuError


class TestOdisseuAgent:
    """Testes para a classe OdisseuAgent"""
    
    @pytest.fixture
    def agent(self):
        """Fixture para criar um agente de teste"""
        return OdisseuAgent(
            api_key="test_key",
            endpoint="http://localhost:8000",
            timeout=30,
            environment="development"
        )
    
    def test_agent_initialization(self, agent):
        """Testar inicialização do agente"""
        assert agent is not None
        assert agent.api_key == "test_key"
        assert agent.endpoint == "http://localhost:8000"
        assert agent.environment == "development"
        assert agent.status == "initialized"
    
    def test_get_info(self, agent):
        """Testar obtenção de informações do agente"""
        info = agent.get_info()
        
        assert info is not None
        assert "name" in info
        assert "version" in info
        assert "status" in info
        assert "capabilities" in info
        assert len(info["capabilities"]) > 0
    
    def test_process_query(self, agent):
        """Testar processamento de query"""
        response = agent.process_query("Como você funciona?")
        
        assert response is not None
        assert "query" in response
        assert "response" in response
        assert "confidence" in response
        assert response["query"] == "Como você funciona?"
    
    def test_process_query_with_context(self, agent):
        """Testar processamento de query com contexto"""
        context = {"user": "test_user", "session": "test_session"}
        response = agent.process_query("Olá", context=context)
        
        assert response is not None
        assert "response" in response
    
    def test_set_session(self, agent):
        """Testar definição de sessão"""
        session_id = "session_123"
        agent.set_session(session_id)
        
        assert agent.session_id == session_id
    
    def test_health_check(self, agent):
        """Testar health check do agente"""
        result = agent.health_check()
        
        assert result is True
        assert agent.status == "healthy"
    
    def test_agent_repr(self, agent):
        """Testar representação em string do agente"""
        repr_str = repr(agent)
        
        assert "OdisseuAgent" in repr_str
        assert "http://localhost:8000" in repr_str


class TestOdisseuIntegration:
    """Testes de integração"""
    
    def test_multiple_queries(self):
        """Testar múltiplas queries"""
        agent = OdisseuAgent(
            api_key="test_key",
            endpoint="http://localhost:8000"
        )
        
        queries = [
            "Olá",
            "Como você funciona?",
            "Qual é a sua função?"
        ]
        
        responses = []
        for query in queries:
            response = agent.process_query(query)
            responses.append(response)
        
        assert len(responses) == len(queries)
        for response in responses:
            assert "response" in response
    
    def test_session_persistence(self):
        """Testar persistência de sessão"""
        agent = OdisseuAgent(
            api_key="test_key",
            endpoint="http://localhost:8000"
        )
        
        session_id = "persistent_session_123"
        agent.set_session(session_id)
        
        # Processar múltiplas queries
        for i in range(3):
            response = agent.process_query(f"Query {i}")
            assert response is not None
        
        # Verificar que session_id é mantido
        assert agent.session_id == session_id


class TestOdisseuEdgeCases:
    """Testes de casos extremos"""
    
    def test_empty_query(self):
        """Testar query vazia"""
        agent = OdisseuAgent(
            api_key="test_key",
            endpoint="http://localhost:8000"
        )
        
        # Deve lidar gracefully com query vazia
        response = agent.process_query("")
        assert response is not None
    
    def test_very_long_query(self):
        """Testar query muito longa"""
        agent = OdisseuAgent(
            api_key="test_key",
            endpoint="http://localhost:8000"
        )
        
        long_query = "teste " * 1000
        response = agent.process_query(long_query)
        assert response is not None
    
    def test_special_characters_in_query(self):
        """Testar caracteres especiais em query"""
        agent = OdisseuAgent(
            api_key="test_key",
            endpoint="http://localhost:8000"
        )
        
        special_query = "Olá! Como vai? #@$%^&*()"
        response = agent.process_query(special_query)
        assert response is not None


class TestOdisseuErrors:
    """Testes de tratamento de erros"""
    
    def test_agent_error_handling(self):
        """Testar tratamento de erros do agente"""
        agent = OdisseuAgent(
            api_key="test_key",
            endpoint="http://localhost:8000"
        )
        
        # O agente deve manter-se estável mesmo com erros
        try:
            response = agent.process_query("teste")
            assert response is not None
        except OdisseuError as e:
            pytest.fail(f"OdisseuError não deve ser levantado: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
