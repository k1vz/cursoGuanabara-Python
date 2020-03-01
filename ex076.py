prod = ("Pão", 1.3,
        "Água", 0.7,
        "Arroz", 11,
        "Pipoca", 3.5,
        "Laranja", 3.7,
        "Caneta", 0.4,
        "Carne", 28)

print('-' * 38)
print(f'{"LISTA DE PREÇOS":^38}')
print('-' * 38)

for i in range(0, len(prod)):
    if i % 2 == 0:
        print(f'{prod[i]:.<30}', end='')
    else:
        print(f'R${prod[i]:>6.2f}')