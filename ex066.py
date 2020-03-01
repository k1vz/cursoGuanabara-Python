n = sn = qn = 0

while True:
    n = int(input("Digite um número [999 == stop]: "))
    if n == 999:
        break
    sn += n
    qn += 1

print(f"A soma total dos {qn} números foi de {sn}.")
