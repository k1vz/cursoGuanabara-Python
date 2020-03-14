print("PRIMEIRA LINHA")
a0 = int(input("Digite um valor pra [0, 0]: "))
a1 = int(input("Digite um valor pra [0, 1]: "))
a2 = int(input("Digite um valor pra [0, 2]: "))

print("\nSEGUNDA LINHA")
b0 = int(input("Digite um valor pra [1, 0]: "))
b1 = int(input("Digite um valor pra [1, 1]: "))
b2 = int(input("Digite um valor pra [1, 2]: "))

print("\nTERCEIRA LINHA")
c0 = int(input("Digite um valor pra [2, 0]: "))
c1 = int(input("Digite um valor pra [2, 1]: "))
c2 = int(input("Digite um valor pra [2, 2]: "))

print(f"""\n| {a0} | {a1} | {a2} |""")
print(f"""| {b0} | {b1} | {b2} |""")
print(f"""| {c0} | {c1} | {c2} |""")

print(f"\nSoma total: {a0 + a1 + a2 + b0 + b1 + b2 + c0 + c1 + c2}")
print(f"Soma total da 3º coluna: {a2 + b2 + c2}")

i = mai = 0

# Checando qual o maior da 3ª linha

while i != 3:
    if i == 0:
        mai = c0
    else:
        if mai < c1:
            mai = c1
        elif mai < c2:
            mai = c2

    i += 1

print(f"O maior valor da 3ª linha é o {mai}.")
