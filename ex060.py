from math import factorial

n = int(input("Digite um número: "))
c = n

while c != 0:
    print(c, end='')
    print(" x " if c != 1 else ' = ', end='')
    c -= 1

print(f"{factorial(n)}.")
