v = float(input("Digite o valor a ser pago: R$"))
print("""-(1) À Vista (dinheiro/cheque): 10% de desconto.
-(2) À vista no cartão: 5% de desconto.
-(3) Em até 2x no cartão: preço normal.
-(4) 3x ou mais no cartão: 20% de juros.""")
p = int(input("Digite a forma de pagamento: "))

if v < 0 or p <= 0 or p > 4:
    print("Digite um valor válido.")
else:
    if p == 1:
        vf = v - (v * 0.1)
        print("\nPreço final: R${:.2f}" .format(vf))
    elif p == 2:
        vf = v - (v * (5/100))
        print("\nPreço final: R${:.2f}" .format(vf))
    elif p == 3:
        print("\nSerão 2 parcelas de R${:.2f} cada. \nPreço final: R${:.2f}" .format(v / 2, v))
    else:
        vf = v + (v * (2/10))
        k = int(input("Digite o número de parcelas: "))
        print("\nSerão {} parcelas de R${:.2f} cada. \nPreço final: R${:.2f}" .format(k, vf / k, vf))
