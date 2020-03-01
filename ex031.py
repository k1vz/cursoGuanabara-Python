import time
dv: float = float(input("Digite a distância da viagem: "))
if dv < 0:
    print("Por favor, digite um valor correto.")
else:
    if dv < 200:
        print("A passagem custará R${:.2f}." .format(dv * 0.5))
    else:
        print("A passagem custará R${:.2f}." .format(dv * 0.45))
