idadeMaiorMedia = list()
galero = list()
mulheres = {'nomes': ''}
somaIdade = i = 0

while True:
    pessoa = dict()
    pessoa['nome'] = str(input("Nome: ")).title().strip()

    # Input seguro de 'sexo';
    pessoa['sexo'] = str(input("Sexo [M/F]: ")).lower().strip()
    while pessoa['sexo'] != 'm' and pessoa['sexo'] != 'f':
        print("ERRO: Digite um valor válido!")
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).lower().strip()

    # Salvando o nome das mulheres;
    if pessoa['sexo'] == 'f':
        mulheres['nomes'] += pessoa['nome'] + ', '

    # Input seguro de 'idade';
    pessoa['idade'] = int(input("Idade: "))
    while pessoa['idade'] <= 0 or pessoa['idade'] > 140:
        print("ERRO: Digite um valor válido!")
        pessoa['idade'] = int(input("Idade: "))

    somaIdade += pessoa['idade']
    galero.append(pessoa)
    i += 1

    # Verificando se o usuário quer continuar;
    c = str(input("\nDeseja continuar? [S/N]: ")).lower().strip()
    while c != 's' and c != 'n':
        c = str(input("Deseja continuar? [S/N]: ")).lower().strip()
    if c == 'n':
        break

# Verificando se as idades são maiores que a média;
for x in galero:
    if x['idade'] > somaIdade / i:
        idadeMaiorMedia.append(x['nome'])

# Output
print('\n' + "-[]-" * (len(f"As mulheres cadastradas foram: {mulheres['nomes'][:-2]}.") // 3))
print(f"{i} pessoas foram cadastradas.")
print(f"As pessoas com idade acima da média são as:")
for y in idadeMaiorMedia:
    print(f"    {y};")
print(f"Idade média foi de: {(somaIdade / i):.1f}.")
print(f"As mulheres cadastradas foram: {mulheres['nomes'][:-2]}.")
print("-[]-" * (len(f"As mulheres cadastradas foram: {mulheres['nomes'][:-2]}.") // 3))
