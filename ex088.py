from random import randint

k = c = 0
n = int(input("Digite quantos jogos você quer: "))
palp = list()

while n != 0: #cada jogo
	for c in range(0, 6): #cada numero
		k = (randint(1, 60))

		if k not in palp:
			palp.append(k)
			pass

	n -= 1
	print("Jogo:", sorted(palp))
	palp.clear()
