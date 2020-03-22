def fatorial(num, show):
    if show:
        for i in range(num, 0, -1):
            if i == 1:
                print(f'{i} = ', end='')
            else:
                print(i, end=" * ")

    i = 1
    for c in range(num, 0, -1):
        i *= c
    print(i)


num = int(input("Digite o número a ser processado: "))
i = input("Mostrar o processo? [S/N]: ").strip().lower()
if i == 's':
    bool = True
elif i == 'n':
    bool = False
else:
    while i != 's' and i != 'n':
        print("\nERRO: Digite um valor válido!")
        i = input("Mostrar o processo? [S/N]: ").strip().lower()

fatorial(num, bool)
