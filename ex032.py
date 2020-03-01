from datetime import date

y = int(input("Digite um ano: "))
if y == 0:
    y = date.today().year

if y < 0:
    print("Você sabe o que é um ano?")
else:
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print("Esse é um ano bissexto.")
    else:
        if y % 4 != 0:
            print("Esse é um ano normal.")
        else:
            print("Esse é um ano normal.")
