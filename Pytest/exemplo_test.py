#Para executar o (PYTEST) python -m pytest "NOME DO AQUIVO"
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4