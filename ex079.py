lista = []
i = '0'

while i != 'n':
  n1 = int(input("Digite algo: "))

  if n1 in lista:
    print("Número já existe na lista, tente outro.")
  else:
    lista.append(n1)

  i = str(input("Deseja continuar? [S/N]: ")).lower().strip()

print(f"\nVocê digitou os valores {sorted(lista)}")
