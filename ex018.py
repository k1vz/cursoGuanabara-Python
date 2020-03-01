import math

a = float(input("Digite o ângulo: "))
sin = math.sin(math.radians(a))
cos = math.cos(math.radians(a))

print("O seno de {} vale {:.2f}, e o cosseno vale {:.2f}." .format(a, sin, cos))