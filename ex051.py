pt = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Digite a razão da P.A.: "))

for i in range(pt, pt + (r * 11), r):
    print(i, end=" -> ")

print("Acabou.")