from time import sleep
from random import randint

p = str(input("Escolha (Pedra/Papel/Tesoura): ")).lower().strip()

if p == "pedra":
    pl = 1
elif p == "papel":
    pl = 2
elif p == "tesoura":
    pl = 3
else:
    print("Por favor escreva corretamente.")
    exit()

pc = randint(1, 3)

if pc == pl:
    print("PROCESSANDO ...")
    sleep(2)
    print("Empate!")
# 1
if pc == 1 and pl == 2:
    print("PROCESSANDO ...")
    sleep(2)
    print("Você venceu!")
if pc == 1 and pl == 3:
    print("PROCESSANDO ...")
    sleep(2)
    print("Você perdeu!")
# 2
if pc == 2 and pl == 1:
    print("PROCESSANDO ...")
    sleep(2)
    print("Você perdeu!")
if pc == 2 and pl == 3:
    print("PROCESSANDO ...")
    sleep(2)
    print("Você venceu!")
# 3
if pc == 3 and pl == 1:
    print("PROCESSANDO ...")
    sleep(2)
    print("Você venceu!")
if pc == 3 and pl == 2:
    print("PROCESSANDO ...")
    sleep(2)
    print("Você perdeu!")
