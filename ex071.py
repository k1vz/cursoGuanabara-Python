cedula: int = 0

while True:
    value = int(input("Digite o valor do saque: "))

    while value != 0:
        if value % 50 == 0:
            cedula += 1
            value -= 50
        elif value % 20 == 0:
            cedula += 1
            value -= 20
            print(value)
        elif value % 10 == 0:
            cedula += 1
            value -= 10
            print('a')
        elif value % 1 == 0:
            cedula += 1
            value -= 1

    print("Número de cédulas: ", cedula)
