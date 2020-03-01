sf = float(input("Digite seu salário atual: "))
if sf <= 0:
    print("Digite um valor válido.")
else:
    if sf > 1250:
        print("Seu novo salário será de R${:.2f}.".format(sf + (sf * (10 / 100))))
    else:
        au = sf * (15 / 100)
        print("Seu novo salário será de R${:.2f}.".format(sf + au))
