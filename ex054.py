from datetime import date

maior: int = 0
menor: int = 0

for i in range(0, 7):
    bd = int(input("Digite o ano de nascimento da {} pessoa: " .format(i+1)))
    
    if 21 <= (date.today().year - bd):
        maior += 1
    else:
        menor += 1

print(f"\nDe 7, {maior} são maiores e {menor} são menores de idade.")