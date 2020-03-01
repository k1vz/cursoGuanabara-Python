h = float(input("Digite o valor da casa: "))
s = float(input("Digite o valor do seu salário: "))
y = int(input("Digite o prazo para pagamento em anos: "))

pm = h / (y * 12)

if pm > (s * (3/10)):
    print("O empréstimo foi NEGADO.")
else:
    print("O empréstimo foi APROVADO.")
