i = error = 0
exp = str(input("Digite a expressão: ")).lower().strip()

for i in exp:
    if error == 0:
        if i == ')':
            print("Sua expressão é inválida.")
            quit()
    if i == '(':
        error += 1
    if i == ')':
        error -= 1

if error == 0:
    print("Sua expressão é válida.")
else:
    print("Sua expressão é inválida.")
