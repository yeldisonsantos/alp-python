from lista import Lista
lista1 = Lista(3)

print("-="*50)

def add(numero):
    if lista1.adicionar(numero) == True:
        print(f"O numero {numero} foi adicionado com sucesso.")
    else:
        print(f"O numero {numero} nao foi adicionado. A lista encheu.")

add(5)
add(7)
# add(8)

print(f"inserindo numero 9 na pos 1... {lista1.inserir(1, 9)}")
print(f"removendo numero que esta na posicao 1... {lista1.remover(1)}")

print(f"Numero 2 esta na lista? {lista1.pesquisar(2)}")
print(f"Numero 5 esta na lista? {lista1.pesquisar(5)}")

print(f"A capacidade da lista é {lista1.capacidade}")
print(f"Lista: {lista1.array}")
print(f"O tamanho da lista: {lista1.tamanho}")

print(f"Existe um valor no indice 1? {lista1.obter(1)}")
print(f"Existe um valor no indice 5? {lista1.obter(5)}")