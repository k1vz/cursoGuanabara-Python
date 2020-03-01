import datetime

nasc = int(input("Digite o ano do seu nascimento: "))
y = (datetime.date.today().year - 18) - nasc

if y < 0:
    print("Você ainda vai se alistar, faltam {} anos para isso." .format(y*(-1)))
elif y == 0:
    print("Está na hora de você se alistar.")
else:
    print("Já se passaram {} anos da hora de você se alistar." .format(y))
