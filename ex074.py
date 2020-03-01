from random import randint

num = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print("Os valores sorteados foram: ", num)

print(f"O menor é o {min(num)}. \nO maior é o {max(num)}.")
