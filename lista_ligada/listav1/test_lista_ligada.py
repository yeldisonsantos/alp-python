from lista_ligada import Lista_Ligada

def test_lista_vazia():
    lista = Lista_Ligada()

    assert lista.tamanho == 0
    assert lista.exibir() == "null"

def test_adicionar():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)
    lista.adicionar(40)

    assert lista.tamanho == 4
    assert lista.exibir() == "10 -> 20 -> 30 -> 40 -> null"
