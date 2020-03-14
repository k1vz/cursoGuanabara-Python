array = list()
par = list()
impar = list()
c = i = g = 0

for i in range(0, 7):
    g = int(input("Digite: "))
    array.append(g)

    if g % 2 == 0:
        par.append(g)
    elif g % 2 == 1:
        impar.append(g)

    g = 0

print(f"\nTodos os números digitados foram: {array}.")
print(f"Números pares digitados: {sorted(par)}.")
print(f"Números ímpares digitados: {sorted(impar)}.")
