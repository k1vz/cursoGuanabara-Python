from random import randint
from time import sleep

pc = randint(0, 10)
us = x = 0

while pc != us:
    x += 1
    us = int(input("Digite um número entre 0 e 10: "))
    if us > 10:
        print("Por favor, digite algo menor que 10.")
    else:
        print("PENSANDO ...")
        sleep(2)  # Laga por 2 seg
        if us < 0:
            print("Por favor, digite algo maior que 0.")
        else:
            if pc == us:
                print("Parabéns você acertou!")
                print(f"Você usou {x} tentativas.")
            else:
                print("Infelizmente você errou.\n")
