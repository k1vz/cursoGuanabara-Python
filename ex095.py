# 'gol', 'c' e 'i' são variáveis para controle;
# 'part_num' é o número total de partidas jogadas.
time = list()

while True:
    jogador = {
        'nome': str(input("Jogador: ")).title().strip(),
        'partidas': {"part_num": int(input("Nº de partidas jogadas: ")), "gols": list()}}

    gol: int = 0
    while jogador['partidas']['part_num'] > gol:
        jogador['partidas']['gols'].append(int(input(f"Nº de gols da {gol + 1}º partida: ")))
        gol += 1

    # Output
    print(f"\nO jogador {jogador['nome']} jogou {jogador['partidas']['part_num']} partidas.")

    time.append(jogador)

    # Verificando se o usuário quer continuar;
    c = str(input("\nDeseja continuar? [S/N]: ")).lower().strip()
    while c != 's' and c != 'n':
        print("ERRO: Digite um valor válido!")
        c = str(input("Deseja continuar? [S/N]: ")).lower().strip()
    if c == 'n':
        break

# Output
print("\n" + '-' * 58)
print("Foram cadastrados os jogadores: ")
for c in time:
    print(' ' * 4 + f"{c['nome']}, que os seguintes gols: {c['partidas']['gols']} com um total de: "
                    f"{sum(c['partidas']['gols'])}.")
print('-' * 58)

while True:
    if c == 99:
        break

    c = int(input("Mostrar dados de qual jogador? [99 = Quit]: "))
    print(f"Dados do {time[c]['nome']}:")
    for i in time[c]['partidas']['gols']:
        print(f"  No jogo {c} ele fez {i} gols.")
        c += 1
