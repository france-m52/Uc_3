# definir a propria exceção. Criar manuelmente
try:
    idade = int(input("Digite sua idade"))
    if idade < 0:
        raise ValueError("A idade não pode seer negativa.")
    print(idade)
except ValueError as ve:
    print(f"Erro: {ve}")