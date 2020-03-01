yq = mq = iq = r = 0

while r != 1:
    c = sx = ''
    yr = int(input("Digite sua idade: "))
    while sx != 'm' and sx != 'f':
        sx = str(input("Digite seu sexo [M/F]: ")).lower().strip()

    print("")

    if yr > 18:
        yq += 1
    if sx == 'm':
        mq += 1
    if sx == 'f' and yr < 20:
        iq += 1

    c = ''

    while c != 's' and c != 'n':
        c = str(input("Você deseja continuar? [S/N]: ")).lower().strip()

        if c == 'n':
            print("Fuck u")
            r = 1

        elif c != 's':
            print("Informe um valor válido.")

print(f"O número de pessoas com mais de 18 anos é de: {yq}.")
print(f"O número de homens cadastrados é de: {mq}.")
print(f"O número de mulheres com menos de 20 é de: {iq}.")
