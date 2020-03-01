menor: float = 0
maior: float = 0

for i in range(0, 5):
    w = float(input("Digite o peso da {}º pessoa: " .format(i + 1)))

    if i == 1:
        menor = w
        menor = w

    if w >= maior:
        maior = w

    if w <= menor:
        menor = w

print(f"\nO maior peso foi {maior}kg, e o menor foi {menor}kg.")
