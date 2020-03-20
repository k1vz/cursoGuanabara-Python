# Input
pessoa = {'nome': str(input("Nome: ")).title().strip(),
          'idade': 2020 - int(input("Ano de nascimento: "))}

# Data Processing
print(f"\nSeu nome é {pessoa['nome']} e você tem {pessoa['idade']} anos.")

if pessoa['idade'] >= 18:
    pessoa['ctps']['num_ctps'] = int(input("Carteira de trabalho [0 se não tiver]: "))

    if pessoa['ctps']['num_ctps'] != 0:
        pessoa['ctps']['y_cont'] = int(input("Ano de sua contratação: "))
        pessoa['ctps']['sal'] = float(input("Salário: "))

        # Data Processing and OutPut
        if pessoa['ctps']['y_cont'] > 1985:
            print(f"Você ainda precisa trabalhar {pessoa['ctps']['y_cont'] - 1985} anos.")
        elif pessoa['ctps']['y_cont'] <= 1985:
            print(f"Você já pode se aposentar :)")
