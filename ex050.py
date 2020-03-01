s: int = 0

for i in range(0, 6):
    n = int(input("Digite o {}º número: " .format(i+1)))

    if n % 2 == 0:
        s = n + s

print("O resultado foi: {}" .format(s))