from pythonds.basic.stack import Stack

n = int(input("Digite um número qualquer: "))
b = str(input("Digite 1 para BINÁRIO.\nDigite 2 para OCTAL.\nDigite 3 para HEXADECIMAL.\nEscolha uma base de "
              "conversão: "))


def divideBy2(decNumber: object) -> object:
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


print(divideBy2(4))
