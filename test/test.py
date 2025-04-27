from src.main import *
from unittest.mock import patch


def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}



def funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()
        yield result

    assert result == {"teste": True, "num_aleatorio": 12345}

