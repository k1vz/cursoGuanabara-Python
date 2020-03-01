ve = float(input('Digite a velocidade atual: '))
if ve > 80:
    print("Você pagou uma multa de: R${:.2f}.".format((ve - 80) * 7))
else:
    print("Tudo na legalidade, patrão.")
