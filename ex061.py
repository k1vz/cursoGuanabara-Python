pt = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Digite a razão da P.A.: "))
x = 0
k = pt

while x < 10:
    print("{}" .format(k), end=', ')
    x += 1
    k = k + r

print("Acabou.")
