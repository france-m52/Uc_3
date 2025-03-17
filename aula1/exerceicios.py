# 1) Faça um programa que leia dois números e mostre a soma, a subtração, a multiplicação e a divisão entre eles.
# num1 = int(input("Digite o primeiro numero"))
# num2 = int(input("Digite outro numero numero"))

# soma = num1 + num2
# sub = num1 - num2
# div = num1 / num2
# mult = num1 * num2

# operacao = input("Qual operação você quer realizar? \n soma = soma \n sub = subtração \n div = divisão \n mult = multiplicação")
# if operacao == "soma":
#     print(f"a soma é {soma}")
# elif operacao == "sub":
#     print(f"a subitração é {sub}")
# elif operacao == "div":
#     print(f"a divisão é {div}")
# elif operacao == "mult":
#     print(f"a mult é {mult}")
# else :
#     print("não reconheci essa operação")

# 2)  Faça um programa que solicite o ano de nascimento do usuário e calcule a sua idade.
# anoNascimento = int(input("Qual o seu ano de nascimento? "))
# idd = 2025 - anoNascimento
# print(f"a sua idade é: {idd}")

# 3) Crie um programa que leia um valor em reais (R$) e mostre o valor convertido em dólares (US$), considerando uma taxa de câmbio fornecida pelo usuário.
# valor1 = float(input("Digite um valor"))
# cambio = float(input("digite a taxa do cambio"))

# converter = valor1 * cambio
# print(f"o valor convertido é de: {converter}")

# 4) Crie um programa que leia três notas de um aluno e calcule a média aritmética.
# alunoNota1 = float(input("Qual a primeira nota? "))
# alunoNota2 = float(input("Qual a segunda nota? "))
# alunoNota3 = float(input("Qual a terceira nota? "))

# media = (alunoNota1 + alunoNota2 + alunoNota3) / 3

# print(f"A média é: {media}")

# 5) Escreva um programa que leia o valor de um produto e o percentual de desconto. O programa deve exibir o valor final com o desconto aplicado.
# valorProduto = float(input("Qual o valor do produto? "))
# percentualDesconto = float(input("Qual o valor do desconto? \n escreva o valor da porcentagem mas sem o simbolo de porcentagem "))

# calcularDesconto = valorProduto * (percentualDesconto / 100)
# valorProdutoFinal = valorProduto - calcularDesconto
# print(f"o valor do produto é: {valorProdutoFinal}")

# 6) Crie um programa que leia uma frase e mostre quantos caracteres ela possui (incluindo espaços).
# frase1 = input("digite uma frase ")
# caracteres = len(frase1)
# print(caracteres)

# 7) Escreva um programa que receba três números inteiros e determine qual deles é o maior.
# num1 = int(input("Digite um número "))
# num2 = int(input("Digite outro número "))
# num3 = int(input("Digite mias um número "))

# if num1 > num2 and num1 > num3:
#     print(f"o maior número é: {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"o maior número é: {num2}")
# elif num3 > num2 and num3 > num1:
#     print(f"o maior número é: {num3}")
# else :
#     print("todos os numeros são iguais")

# 8) Escreva um programa para ler o salário de um funcionário, e calcular o IRPF que precisa ser descontado do salário.
# No Brasil, a tabela do Imposto de Renda para pessoas físicas (IRPF) é progressiva, ou seja, as alíquotas aumentam conforme a renda do contribuinte. A tabela é ajustada anualmente e varia de acordo com a faixa de salário. Para o ano de 2024, as faixas de tributação do Imposto de Renda para pessoas físicas são as seguintes:Até R$ 2.112,00: isento (não paga imposto de renda)
# De R$ 2.112,01 até R$ 2.826,65: 7,5% (aplica-se sobre o valor que exceder a R$ 2.112,00)
# De R$ 2.826,66 até R$ 3.751,05: 15% (aplica-se sobre o valor que exceder a R$ 2.826,65)
# De R$ 3.751,06 até R$ 4.664,68: 22,5% (aplica-se sobre o valor que exceder a R$ 3.751,05)
# Acima de R$ 4.664,68: 27,5% (aplica-se sobre o valor que exceder a R$ 4.664,68)

# salario = float(input("Qual é o seu sálario?"))
# if salario <=2112:
#     print("seu salario é isento de IRPJ")
# elif salario > 2122 and salario <= 2826.65:
#     irpj = salario * (7.5 / 100)
#     print(f"O seu irpj é: {irpj}")
# elif salario > 2826.66 and salario <= 3751.05:
#     irpj = salario * (15 / 100)
#     print(f"O seu irpj é: {irpj}")
# elif salario > 3751.06 and salario <= 4664.68:
#     irpj = salario * (22.5 / 100)
#     print(f"O seu irpj é: {irpj}")
# else:
#     irpj = salario * (27.5 / 100)
#     print(f"O seu irpj é: {irpj}")

# 9) Crie um programa que calcule o valor total de uma compra feita em várias parcelas.
# Pergunte ao usuário quantas parcelas ele deseja e o valor de cada uma.
# Se o total ultrapassar R$ 1.000,00, acrescente 5% de juros.

# produto = float(input('Digite o valor do produto: R$ '))
# parcelas = float(input('Em quantas parcelas você deseja pagar: '))
# produtoParceladomes = 0

# if (produto <= 1000):
#     produtoParceladomes = (produto / parcelas)
#     print(f'Você pagará ao mês R$ {produtoParceladomes:.2f}.')
#     print(f'E o total ficará: R$ {produtoParceladomes * parcelas:.2f}.')
   
# else:
#     produto = (produto + (produto * 0.05))  
#     produtoParceladomes = (produto / parcelas)
#     print(f'Você pagará ao mês R$ {produtoParceladomes:.2f} devido ao acréscimo de 5% ao exceder o valor de R$ 1.000,00.')
#     print(f'E o total ficará: R$ {produtoParceladomes * parcelas:.2f}.')

# 10) Considere que o preço da tarifa de energia é R$ 0,50 por kWh. Pergunte ao usuário o consumo de energia em kWh e calcule o valor total a ser pago pela conta. Se o consumo for maior que 200 kWh, aplique um desconto de 10%.
    
# 11) Crie um programa que calcule o tempo restante até a aposentadoria de uma pessoa. Pergunte a idade e o tempo de contribuição (em anos). A pessoa pode se aposentar com 35 anos de contribuição ou 60 anos de idade. Mostre o tempo restante para a aposentadoria.
    
# 12) ler 3 valores e verificar se podem ser lados de um triangulo e informar caso afirmativo, qual é o triangulo.
    
# 13) ler altura e peso, e informar o imc e qual a situação do indivíduo.
    
# 14) Solicita um valor e um percentual de desconto, e calcula o valor final.
    
# 15) Solicita três notas de um aluno, calcular a média e informar se ele está aprovado ou não, considerando a média de aprovação maior ou igual a 6.
    
# 16) Verifica se uma pessoa tem idade suficiente para dirigir.