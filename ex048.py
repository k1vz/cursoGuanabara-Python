s: int = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        s = i + s

print("O total foi de: ", s)
