h: int = 0

while h != 5:
    n1 = float(input("Digite um valor: "))
    n2 = float(input("Digite outro valor: "))
    print("")
    print("Escolha uma opção. \n [1] Somar.\n [2] Multiplicar. \n [3] Maior. \n [4] Novos números. \n [5] Sair do "
          "programa.")
    h = int(input("Qual a opção desejada? "))
    print("")

    if h == 1:
        r = n1 + n2
        print("O resultado é igual a {}." .format(r))
    elif h == 2:
        r = n1 * n2
        print("O resultado é igual a {}." .format(r))
    elif h == 3:
        if n1 > n2:
            print("O {} é maior.".format(n1))
        else:
            print("O {} é maior.".format(n2))
    elif h == 4:
        pass
    elif h == 5:
        exit(0)
    else:
        print("Digite um valor válido.")

    if h == 4:
        pass
    else:
        print("")
