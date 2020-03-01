par = ninex = threef = 0

num = (int(input("Digite um valor: ")),
       int(input("Digite outro valor: ")),
       int(input("Digite outro valor: ")),
       int(input("Digite outro valor: ")))

for pos, i in enumerate(num):
    if i == 9:
        ninex += 1
    if threef == 0:
        if i == 3:
            threef = pos
    if i % 2 == 0:
        par += 1

print(f"\nO número 9 apareceu {ninex} vezes.")
print(f"A primeira vez que o 3 apareceu foi na {threef + 1}º posição.")
print(f"Tiveram {par} números pares.")
