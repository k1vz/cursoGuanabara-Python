n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

if n1 > n2:
    print("O primeiro valor ({}) é maior." .format(n1))
elif n2 > n1:
    print("O segundo valor ({}) é maior." .format(n2))
else:
    print("Não existe valor maior, os dois são iguais.")
