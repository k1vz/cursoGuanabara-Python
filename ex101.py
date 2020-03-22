from datetime import date
yt = date.today().year


def voto(y):
    y = yt - y
    if y < 16:
        print(f"Com {y} anos seu voto é negado.")
    elif y < 18 or 65 < y < 130:
        print(f"Com {y} anos seu voto é opcional.")
    elif y < 65:
        print(f"Com {y} anos seu voto é obrigatório.")
    else:
        print("\nVocê realmente existe? '-'")


yu = int(input("Ano de nascimento: "))
voto(yu)
