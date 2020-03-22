def leiaInt(y):
    n = input(y)
    try:
        n = int(n)
        print(f"Você digitou o número {n}.")
    except ValueError:
        print("ERRO: O valor digitado NÃO é um número!")
        quit()


leiaInt("Digite um número: ")
