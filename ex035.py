n1 = float(input("Digite o comprimento da reta 1: "))
n2 = float(input("Digite o comprimento da reta 2: "))
n3 = float(input("Digite o comprimento da reta 3: "))

if n1 > n2 and n1 > n3:
    if n2 + n3 >= n1:
        print("Elas podem formar um triângulo.")
    else:
        print("Elas não podem formar um triângulo.")
elif n2 > n1 and n2 > n3:
    if n1 + n3 >= n2:
        print("Elas podem formar um triângulo.")
    else:
        print("Elas não podem formar um triângulo.")
elif n3 > n1 and n3 > n2:
    if n1 + n2 >= n3:
        print("Elas podem formar um triângulo.")
    else:
        print("Elas não podem formar um triângulo.")
