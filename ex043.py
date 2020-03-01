from time import sleep

p = float(input("Digite seu peso (Kg): "))
h = float(input("Digite sua altura (Cm): "))

imc = p / (h/100)**2

if p < 0 or h < 0 or h > 250 or p > 300:
    print("\n")
    print("Xx" * 17)
    print("Por favor, digite um valor válido.")
    print("Xx" * 17)
else:
    if imc < 18.5:
        print("Abaixo do peso.")
    elif imc < 25:
        print("Peso ideal. ;)")
    elif imc < 30:
        print("Sobrepeso.")
    elif imc < 40:
        print("Obesidade.")
    else:
        print("3 ...")
        sleep(1)
        print("2 ...")
        sleep(1)
        print("1 ...")
        sleep(1)
        print("Vá em paz ='(")
