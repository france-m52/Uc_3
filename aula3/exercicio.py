# 1. Escreva um programa que receba números inteiros do usuário até que um número negativo seja digitado. Exiba a soma de todos os números positivos digitados.

# soma = 0
# i = 10
# while i >= 0:
#     i = int(input("digite um numero "))
#     if i >= 0:
#         soma += i
# else:
#     print(f"a soma foi {soma}")

# 2. Escreva um programa que exiba a tabuada de multiplicação de um número digitado pelo usuário, de 1 a 10.

# tabuada = int(input("digite um numero que você seja pegar a tabuada"))

# for i in range(1,11):
#     print(f"{tabuada} x {i} é: {tabuada * i}")

# 3. Crie um programa que utilize um loop while para exibir os números de 1 a 20 na tela.

# i = 0
# while i < 20:
#   i+=1
#   print(i)

# 4. Solicite ao usuário 5 números e exiba a soma total, usando um loop

# q1 = int(input("digite um numero"))
# q2 = int(input("digite outro numero"))
# q3 = int(input("digite mais um numero"))
# q4 = int(input("digite outro numero"))
# q5 = int(input("digite novamente mais um numero"))

# soma = 0
# fruits = ["q1", "q2", "q3", "q4", "q5"]
# for x in fruits:
#   print(f"{soma + lan(fruits)}")

# soma = 0

# for i in range(5):
#     numero = int(input(f"Digite {i+1}° número "))
#     soma += numero
# print(f"A soma dos números é {soma}")

# 5. Solicite um nome ao usuário e peça a quantidade de vezes que ele deseja exibi-lo na tela. Utilize um loop while.

nome = input("Qual o seu nome?")
quantidade = int(input("Quantas vezes quer que ele apareça?"))
i = 0
while i <= quantidade:
    if i <= quantidade:
     i+=1
    print(f"{nome}")


# 6. Escreva um programa que receba 10 números inteiros e conte quantos deles são pares.

# 7. Leia o nome do time de 10 torcedores, e ao final informe quantos são flamenguistas, vascaínos, tricolores, botafoguenses, ou outro time.

# 8. Escreva um programa que receba números inteiros até que o usuário digite 0. Calcule e exiba a média dos números positivos digitados.

# 9. Escreva um programa para ler o salário e o sexo de vários funcionários
# (defina uma cláusula para terminar a leitura) ao término, informar a média de salário de homens e mulheres

# 10.  Leia o salario e o sexo de n funcionários, e ao final informe:
# - qtd de funcionários de cada sexo
# - a soma do salário das mulheres
# - a soma do salário dos homens
# - a média salarial dessa empresa
# - o programa termina quando for digitado "fim"

# 11. Crie um programa que calcule o consumo total de energia de vários aparelhos em uma casa. Pergunte o consumo de cada aparelho em kWh e a quantidade de horas que o aparelho fica ligado por dia. O programa deve somar o consumo diário de todos os aparelhos e calcular o custo total de energia no mês.