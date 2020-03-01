n = int(input("Digite o número: "))

for i in range(2, n):
    if n % i == 0:
        print("Não é primo.")
        exit(0)

print("É primo.")
