from datetime import date

nasc = int(input("Digite o ano que você nasceu: "))
y = date.today().year - nasc

if y > 20:
    print("Sua categoria é a MASTER.")
elif y > 19:
    print("Sua categoria é a SÊNIOR.")
elif y > 14:
    print("Sua categoria é a JÚNIOR.")
elif y > 9:
    print("Sua categoria é a INFANTIL.")
else:
    print("Sua categoria é a MIRIM.")
