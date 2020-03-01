i = sn = qn = 0

while i != 999:
    sn += i
    pass
    qn += 1
    i = float(input("Digite um número: "))

print("\nForam {} números digitados." .format(qn - 1))
print("A soma total foi de: {:.2f}." .format(sn))
