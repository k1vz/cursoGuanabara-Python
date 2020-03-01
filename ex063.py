from math import sqrt, pow

n = int(input("Digite um número: "))
print("{}" .format((1 / sqrt(5)) * (pow((1 + sqrt(5)) / 2, n) - pow((1 - sqrt(5)) / 2, n))))
print("{:.0f}" .format((1 / sqrt(5)) * (pow((1 + sqrt(5)) / 2, n) - pow((1 - sqrt(5)) / 2, n))))
#(1 / sqrt(5)) * (pow((1 + sqrt(5)) / 2, n) - pow((1 - sqrt(5)) / 2, n))
#(1 / sqrt(5)) * (((1 + sqrt(5)) / 2)^x - ((1 - sqrt(5)) / 2)^x)


'''
n = int(input("Digite um número: "))
a = i = c = 0
b = 1

while n != i:
    print(f"{a}", end='')
    print(" -> " if n != i + 1 else '.', end='')
    c = a + b
    a = b
    b = c
    i += 1
'''