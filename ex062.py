pt = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Digite a razão da P.A.: "))
x = 0
i = 1
k = pt

while i != 0:
    x = x - i
    while x < 10:
        print("{}" .format(k), end='')
        print(" -> " if x != 9 else '.', end='')
        x += 1
        k = k + r

    i = int(input("\nDigite quantos termos da P.A. você quer ver: "))

print("Acabou.")
