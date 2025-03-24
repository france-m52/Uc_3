# compressão de listas
# exemplos 2 (enumeração de listas)
lista = ['abacate','abacaxi','melao','ameixão','maçã']
for i in range(len(lista)):
    print(i, lista[1])

#A função enumerrete() em python é usado para iterar sobre uma sequência
#como uma lista, tupla ou string) e obter tanto o indice (posição) quanto o
#valor de cada item da sequencia ao mesmo tempo.
for i, fruta in enumerate(lista):
        print(i, fruta)

texto = "Python"

for indice, caracter in enumerate(texto):
      