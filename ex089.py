turma = list()
i = c = 0

while i != 'n':
	aluno = list()

	# Pegando o nome do aluno.
	c += 1
	nome = str(input(f"Digite o nome do aluno {c}: "))
	aluno.append(nome)

	# Pegando as duas notas do aluno. Com verificação de erro de digitação do usuário.
	nota1 = float(input("Digite a nota 1: "))
	while not 0 <= nota1 <= 10:
		print("\nALERTA: Digite algo entre 0 e 10!")
		nota1 = float(input("Digite a nota 1: "))
	nota2 = float(input("Digite a nota 2: "))

	while not 0 <= nota2 <= 10:
		print("\nALERTA: Digite algo entre 0 e 10!")
		nota2 = float(input("Digite a nota 2: "))
	nota_media = (nota1 + nota2) / 2

	# Inserindo tudo em seu devido lugar e excluindo o a lista 'aluno'.
	aluno.append(nota_media)
	turma.append(aluno)
	del aluno

	# Verificando se o usuário deseja continuar.
	i = str(input("Deseja continuar? [S/N]: ")).lower().strip()
	while i != 's' and i != 'n':
		print("\nALERTA: Digite S/N!")
		i = str(input("Deseja continuar? [S/N]: ")).lower().strip()

	print('')

for c in turma:
	print(f"Nome: {c[0]} Nota: {c[1]:.1f}.")
