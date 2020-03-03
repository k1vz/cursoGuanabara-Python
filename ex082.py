lista = []
lista_par = []
lista_impar = []
i = '0'

while i != 'n':
    n1 = int(input("Digite algo: "))
    lista.append(n1)

    if n1 % 2 == 0:
        lista_par.append(n1)
    else:
        lista_impar.append(n1)

    i = str(input("Deseja continuar? [S/N]: ")).lower().strip()

    while i != 's' and i != 'n':
        i = str(input("Deseja continuar? [S/N]: ")).lower().strip()

print(f"\nVocê digitou os valores {lista}")
print(f"Os pares digitados foram: {lista_par}")
print(f"Os ímpares digitados foram: {lista_impar}")
