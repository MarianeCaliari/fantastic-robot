import random
from unittest.mock import patch

# Sua função:
def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 20000)}

# Testes:
def test_funcaoteste_valores():
    # Mock do random.randint para sempre retornar 12345
    with patch('random.randint', return_value=12345):
        resultado = funcaoteste()
        assert resultado == {"teste": True, "num_aleatorio": 12345}

def test_funcaoteste_tipo():
    resultado = funcaoteste()
    assert isinstance(resultado, dict)
    assert "teste" in resultado
    assert "num_aleatorio" in resultado
    assert isinstance(resultado["teste"], bool)
    assert isinstance(resultado["num_aleatorio"], int)
    assert 0 <= resultado["num_aleatorio"] <= 20000

