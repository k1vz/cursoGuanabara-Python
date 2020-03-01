from time import sleep

n1 = float(input("Digite o comprimento da reta 1: "))
n2 = float(input("Digite o comprimento da reta 2: "))
n3 = float(input("Digite o comprimento da reta 3: "))
print("PROCESSANDO ...\n")
sleep(1)
x = 0

if n1 >= n2 and n1 >= n3:
    if n2 + n3 >= n1:
        print("Elas podem formar um triângulo.")
    else:
        x = 1
        print("Elas não podem formar um triângulo.")
elif n2 >= n1 and n2 >= n3:
    if n1 + n3 >= n2:
        print("Elas podem formar um triângulo.")
    else:
        x = 1
        print("Elas não podem formar um triângulo.")
elif n3 >= n1 and n3 >= n2:
    if n1 + n2 >= n3:
        print("Elas podem formar um triângulo.")
    else:
        x = 1
        print("Elas não podem formar um triângulo.")

if x == 0:
    if n1 == n2 and n1 == n3:
        print("Triângulo equilátero.")
    elif  n1 == n2 or n2 == n3 or n1 == n3:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")
