ppl = list()
dado = list()
i = h = hpeso = hppl = mpeso = mppl = 0

while i != 'n':
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Peso: ")))
    ppl.append(dado[:])
    dado.clear()

    i = str(input("\nDeseja continuar? [S/N]: ")).lower().strip()

    while i != 's' and i != 'n':
        i = str(input("Deseja continuar? [S/N]: ")).lower().strip()

    # Checando Peso
    for p in ppl:
        if h == 1:
            hpeso = p[1]
            hppl = p[0]
            mpeso = p[1]
            mppl = p[0]
        elif p[1] > hpeso:
            hpeso = p[1]
            hppl = p[0]
        elif p[1] < mpeso:
            mpeso = p[1]
            mppl = p[0]

        h += 1

print('=' * 40)
print(f"{h} pessoas foram cadastradas.")
print(f"O maior peso foi do {hppl}, que tem {hpeso} kilos.")
print(f"O menor peso é do {mppl}, que tem {mpeso} kilos.")
