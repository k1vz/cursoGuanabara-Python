num_ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

num = int(input("Digite um número [0 < x > 20]: "))

if 0 > num or num > 20:
    print("Tu é bosta, roda denovo.")
    quit()
else:
    print(f"Você digitou o número {num_ext[num]}.")
