d = float(input("Digite a distância percorrida: "))
t = int(input("Digite o número de dias com o carro: "))
pf = (t*60)+(0.15*d)

print("O preço total é igual a R${:.2f}." .format(pf))