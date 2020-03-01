f = str(input("Digite um frase: ")).lower().strip()
a = f.replace(' ', '')
b = a[::-1]

if b == a:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")