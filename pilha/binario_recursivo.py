def binario(numero):
  if numero < 2:
    return str(numero)
  return binario(numero // 2)  + str(numero % 2)

numero = int(input("Digite um número: "))
print(f"Binário: {binario(numero}")
