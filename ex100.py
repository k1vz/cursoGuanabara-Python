from random import randint
from time import sleep
array = list()


def sorteia():
    print(f"Sorteando 5 números: ", end='')
    for i in range(0, 5):
        c = randint(0, 10)
        array.append(c)
        sleep(1)
        print(c, end=', ')


def soma():
    somatotal: int = 0
    for i in array:
        if i % 2 == 0:
            somatotal += i
    print(f"e a soma total dos pares é: {somatotal}.")


sorteia()
soma()
