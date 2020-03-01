from random import randint
from time import sleep

pc = randint(0, 5)
us = int(input("Digite um número entre 0 e 5: "))
if us > 5:
    print("Por favor, digite algo menor que 5.")
else:
    print("PENSANDO ...")
    sleep(2)  # Laga por 2 seg
    if us < 0:
        print("Por favor, digite algo maior que 0.")
    else:
        if pc == us:
            print("Parabéns você acertou!")
        else:
            print("Infelizmente você errou.")
