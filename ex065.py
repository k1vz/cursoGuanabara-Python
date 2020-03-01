i = mn = mx = sn = x = 0
pl: str = 's'

while pl == 's':
    n = int(input("Digite um número: "))

    if i == 0:
        mn = n
        mx = n
    else:
        if n < mn:
            mn = n
        elif n > mx:
            mx = n

    sn = n + sn
    i += 1
    x = 0

    while x == 0:
        pl = str(input("Deseja continuar? [S/N]: ")).lower().strip()
        x = 1

        if pl != 's' and pl != 'n':
            print("\nDigite um valor válido.")
            x = 0

    print('')

print("\nA soma total foi de: {}." .format(sn))
print("A média de todos os números foi de {}." .format(sn / i))
print(f"O menor valor digitado foi {mn}.")
print(f"E o maior valor digitado foi {mx}.")
