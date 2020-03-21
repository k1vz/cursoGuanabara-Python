def contador(pt, f, r):
    for i in range(pt, f + 1, r):
        print(i, end=" -> ")


contador(1, 10, 1)
print()
contador(10, 0, -2)
print()
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Razão: ")))
