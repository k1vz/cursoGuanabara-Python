def notas(nt, sit=False):
    """ Uma função que tem uma série de funções sobre um certo número de notas digitadas. """
    print(f"\nForam informadas {len(nt)} notas.")
    print(f"A maior nota inserida foi: {max(nt)}.")
    print(f"A menor nota inserida foi: {min(nt)}.")
    print(f"A média de todas as notas é: {(sum(nt) / len(nt)):.1f}.")
    if sit:
        if sum(nt) / len(nt) > 7:
            print("Situação: aprovado.")
        elif sum(nt) / len(nt) > 6:
            print("Situação: em recuperação.")
        else:
            print("Situação: reprovado.")


i = n = 0
array = list()

while n != -1:
    i += 1
    n = int(input(f"Digite a {i}ª nota [-1 Finish]: "))
    if n != -1:
        array.append(n)

i = input("Você deseja ver a situação do aluno? [S/N]: ").lower().strip()
if i == 's':
    i = True
else:
    i = False

notas(array, i)
