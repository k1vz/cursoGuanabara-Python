from time import sleep


def maior(num):
    print('-=' * 20)
    print('Analisando ...')
    sleep(2)
    for i in num:
        print(i, end=' ')

    if len(num) > 0:
        print(f"- foram informados {len(num)} valores.")
        print(f"O maior valor informado foi o {max(num)}.")
    else:
        print("Nenhum valor foi informado.")


maior([2, 3, 5])
maior([4, 7, 0])
maior([1, 2])
maior([6])
maior([])
