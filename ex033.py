n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite outro número: "))

if n1 > n2 and n1 > n3:
    print("O {} é o maior entre eles." .format(n1))
    if n2 < n3:
        print("E o {} é o menor entre eles." .format(n2))
    else:
        print("E o {} é o menor entre eles." .format(n3))
elif n2 > n1 and n2 > n3:
    print("O {} é o maior entre eles." .format(n2))
    if n1 < n3:
        print("E o {} é o menor entre eles." .format(n1))
    else:
        print("E o {} é o menor entre eles." .format(n3))
elif n3 > n1 and n3 > n2:
    print("O {} é o maior entre eles." .format(n3))
    if n1 < n2:
        print("E o {} é o menor entre eles." .format(n1))
    else:
        print("E o {} é o menor entre eles." .format(n2))
else:
    print("Poxa menor.")
