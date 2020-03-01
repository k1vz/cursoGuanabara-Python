from time import sleep

ys: int = 0
y_old: int = 0
n_old: str
w_tw: int = 0

for i in range(0, 4):
    name = str(input("Digite o nome da {}º pessoa: " .format(i + 1)))
    year = int(input("Digite a idade de {}: " .format(name)))
    sex = int(input("Digite 1 para masculino ou 2 para feminino: "))

    ys = year + ys

    if sex == 1:
        if year >= y_old:
            n_old = name

    if sex == 2:
        if year <= 20:
            w_tw += 1

    print("")

print("\n" + "Xx" * 20)
print("O RESULTADO ESTÁ FICANDO PRONTO ...")
print("Xx" * 20 + "\n")
sleep(3)
print("A média de idade do grupo é de {:.2f} anos de idade." .format(ys / 4))
print("O nome da pessoa mais velha é: {}." .format(n_old))
print("O número de mulheres com menos de 20 anos é de: {}." .format(w_tw))
