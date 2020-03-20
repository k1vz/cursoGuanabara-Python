# 'gol' e 'c' são variáveis para controle.
# 'part_num' é o número total de partidas jogadas.

jogador = {
    'nome': str(input("Jogador: ")).title().strip(),
    'partidas': {"part_num": int(input("Nº de partidas jogadas: ")), "gols": list()}}

gol: int = 0
while jogador['partidas']['part_num'] > gol:
    jogador['partidas']['gols'].append(int(input(f"Nº de gols da {gol + 1}º partida: ")))
    gol += 1

# Output
print(f"\nO jogador {jogador['nome']} jogou {jogador['partidas']['part_num']} partidas.")

c: int = 0
for gol in jogador['partidas']['gols']:
    c += 1
    print(f"   > Na {c}º partida ele fez {gol} gols.")

print(f"Foi um total de {sum(jogador['partidas']['gols'])} gols.")
