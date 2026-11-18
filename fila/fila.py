from lista_ligada import ListaLigada

class Fila:
    def __init__(self):
        self._elementos = ListaLigada()

    def empilhar(self, item):
        self._elementos.adicionar(item)

    def desempilhar(self):
        self._elementos.remover_inicio()

    def topo(self):
        if self.vazia():
            return None
        return self._elementos.primeiro.item

    def vazia(self):
        return self._elementos.vazia()

    def tamanho(self):
        return self._elementos.tamanho
