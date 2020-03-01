n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
m = (n1 + n2) / 2

if n1 > 10 or n2 > 10 or n1 < 0 or n2 < 0:
    print("Digite um valor válido.")
else:
    if m >= 7:
        print("Aprovado.")
    elif m >= 5:
        print("Recuperação.")
    else:
        print("Reprovado.")
