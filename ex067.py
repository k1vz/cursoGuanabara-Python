while True:
    n = int(input("\nDigite o número desejado: "))

    if n < 0:
        exit()
    else:
        for d in range(1, 11):
            print(f"{n} x {d} = {n * d}")
