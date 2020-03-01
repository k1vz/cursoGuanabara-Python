x: int = 0
while x == 0:
    sex = str(input("Digite seu sexo [M/F]: ")).lower().strip()[0]

    if sex == 'm' or sex == 'f':
        x = 1
    else:
        print("Digita algo decente fdp.\n")

print(f"Sexo {sex.upper()} registrado corretamente.")