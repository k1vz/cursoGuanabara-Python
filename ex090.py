aluno = {}
aluno = {'nome': str(input("Nome: ")), 'media': float(input("Média: "))}
print(f"\nO aluno {aluno['nome']}, que possui a média {aluno['media']} e esse aluno está", end='')
if aluno['media'] > 7:
    print(" aprovado.")
else:
    print(" reprovado.")
