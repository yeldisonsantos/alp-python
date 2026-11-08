from lista_ligada import ListaLigada
import pytest

@pytest.fixture
def lista():
    lista = ListaLigada()
    lista.inserir_inicio(10)
    lista.inserir_inicio(20)
    lista.inserir_inicio(30)
    lista.inserir_inicio(40)
    return lista

def test_exibir_lista(lista):
    assert str(lista) == "40 -> 30 -> 20 -> 10 -> null"

def test_inserir_inicio(lista):
    lista.inserir_inicio(1)
    assert lista.primeiro.item == 1
    assert str(lista) == "1 -> 40 -> 30 -> 20 -> 10 -> null"

def test_pesquisar(lista):
    assert lista.pesquisar(30) == True

def test_obter(lista):
    assert lista.obter(1) == 30

def test_inserir(lista):
    lista.inserir(1, 15)
    assert str(lista) == "40 -> 15 -> 30 -> 20 -> 10 -> null"

def test_remover_inicio(lista):
    lista.remover_inicio()
    assert str(lista) == "30 -> 20 -> 10 -> null"

def test_remover(lista):
    # lista.remover(0)
    # assert str(lista) == "30 -> 20 -> 10 -> null"
    lista.remover(1)
    assert str(lista) == "40 -> 20 -> 10 -> null"

def test_remover_item(lista):
    lista.remover_item(40)
    assert str(lista) == "30 -> 20 -> 10 -> null"

if __name__ == "__main__":
    pytest.main(["-v"])
