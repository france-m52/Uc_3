#professor pedia pra gente fazer uma apresetação sobre list, pra qure ela serve e sua função
#exemplos utilizados]

inventario = ["espada", "poção", "escudo"]# vai imprimir todos os itens dentro da lista
print(inventario)

inventario = ["espada", "poção", "escudo"]
print(inventario[0])#vai imprimir o intem na posição zero, nesse caso a espada

inventario[0] = "livro magico"  # Mudando o primeiro elemento

inventario.append("bota de ouro")  # Adicionando um novo elemento

#uma list ie uma coleção, ordenada ou seja seguebuma ordem logica (0,1,2,3...) é utavel e permite itens duplicados.

inventario2 = ["escudo", "espada", "madeira", "poção de vitalidade", "bandagem"]
print(inventario2[1:4])  # [espada, madeira, poção de vitalidade] (itens do índice 1 ao 3)

# Listas possuem vários métodos para manipulação. Alguns dos mais usados são:

# append(x): Adiciona um item no final da lista.

# insert(i, x): Insere um item na posição especificada.

# remove(x): Remove o primeiro item da lista que tem o valor x.

# pop(i): Remove e retorna o item na posição i.

# sort(): Ordena a lista.

# reverse(): Inverte a lista.

#EXEMPLO

lista = [3, 1, 2]
lista.append(4)  # Adiciona 4 no final
lista.sort()     # Ordena a lista
print(lista)  # [1, 2, 3, 4]

#se você colocar
print(lista[-1])
# ele vai mostrar o ultimp elemento da lista e assim sucessivamente