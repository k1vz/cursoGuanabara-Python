frase = str(input("Digite uma frase: ")).lower().strip()
print("O 'a' aparece {} vezes." .format(frase.count("a")))
print("A primeira vez que ela aparece é na {}º posição." .format(frase.lower().find("a") + 1))
print("A última vez que ela apareceu foi na {}º posição." .format(frase.lower().rfind("a") + 1))