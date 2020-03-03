lista = []
i = '0'
c = 0

while i != 'n':
    n1 = int(input("Digite algo: "))

    if n1 in lista:
        print("Número já existe na lista, tente outro.")
    else:
        lista.append(n1)

    i = str(input("Deseja continuar? [S/N]: ")).lower().strip()

    while i != 's' and i != 'n':
        i = str(input("Deseja continuar? [S/N]: ")).lower().strip()

print(f"\nVocê digitou os valores {sorted(lista, reverse = True)}.")
print(f"Você digitou {len(lista)} valores.")

if 5 in lista:
    print("O 5 está na lista.")
else:
    print("O 5 NÃO está na lista.")
