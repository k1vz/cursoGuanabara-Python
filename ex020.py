from random import shuffle

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")
classe = [a1, a2, a3, a4]
esc = shuffle(classe)

print("A ordem ficou: ", classe)