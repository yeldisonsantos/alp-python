class Lista:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.array = [None] * self.capacidade
        self.tamanho = 0

    def adicionar(self, numero):
        if self.tamanho < self.capacidade:
            self.array[self.tamanho] = numero
            self.tamanho += 1
            return True
        return False

    def pesquisar(self, numero):
        for i in range(self.tamanho):
            if self.array[i] == numero:
                return True
        return False

    def obter(self, posicao):
        if 0 <= posicao < len(self.array) and self.array[posicao] != None:
            return self.array[posicao]
        return None

    def inserir(self, posicao, numero):
        if self.tamanho < self.capacidade and 0 <= posicao <= self.tamanho:
            for i in range(self.tamanho, posicao, -1):
                self.array[i] = self.array[i-1]
            self.array[posicao] = numero
            self.tamanho += 1
            return True
        return False

    def remover(self, posicao):
        if 0 <= posicao < self.tamanho:
            for i in range(posicao, self.tamanho-1):
                self.array[i] = self.array[i+1]
            self.array[self.tamanho-1] = None
            self.tamanho -= 1
            return True
        return False