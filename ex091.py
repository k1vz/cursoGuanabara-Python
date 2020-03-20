from random import randint

pg = {}
for i in range(1, 5):
    pg['jogador ' + str(i)] = randint(1, 6)
    i += 1

for k, v in pg.items():
    if k == "jogador 1":
        m1n = m4x = v
        pmax = pmin = k
    elif m1n > v:
        m1n = v
        pmin = k
    elif m4x < v:
        m4x = v
        pmax = k

    print(f"O {k}, tirou {v} no dado.")

print(f"\nO maior valor tirado foi {m4x} pelo {pmax}.")
print(f"O menor valor tirado foi {m1n} pelo {pmin}.")
