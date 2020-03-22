def ficha(nome='não informado', gols='um número indefinido de'):
    print(f"O jogador {nome} marcou {gols} gols.")


nome = input("Nome do jogador: ").strip().title()
gols = input("Gols: ")
if gols != '':
    gols = int(gols)

if nome != '' and gols != '':
    ficha(nome, gols)
elif nome != '':
    ficha(nome)
elif gols != '':
    ficha(gols=gols)
