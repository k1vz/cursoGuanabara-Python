i = totprice = price1k = lowestprice = price = 0
lowestpricenm: str = ''

while True:
    name = str(input("Digite o nome: ")).lower().strip()
    price = float(input("Digite o preço: R$"))

    totprice += price

    if price > 1000:
        price1k += 1

    if i == 0:
        lowestprice = price
        lowestpricenm = name
    elif lowestprice >= price:
        lowestprice = price
        lowestpricenm = name

    i += 1

    stop = str(input("Deseja continuar? [S/N]: ")).lower().strip()
    print("")

    if stop == 'n':
        break
    elif stop == 's':
        pass

print(f"O total gasto foi de R${totprice:.2f}.")
print(f"O número de produtos que custam mais de 1k é: {price1k}.")
print(f"O nome do produto mais barato é: {lowestpricenm}.")
