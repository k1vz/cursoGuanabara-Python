from random import randint

qn = 0

while True:
    pl = int(input("Escolha [PAR = 0] ou [ÍMPAR = 1]: "))
    print("")

    if pl != 0 and pl != 1:
        print("Digite um valor correto.")
    else:
        pc = randint(0, 1)

        if pl == pc:
            print("Você ganhou!")
            qn += 1
            pass
        else:
            print("Você perdeu!")
            print(f"Você ganhou {qn} veze(s).")
            exit()
