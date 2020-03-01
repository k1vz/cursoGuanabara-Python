h = int(input("Altura da parede: "))
l = int(input("Comprimento da parede: "))
a = (h*l)
t = (a/2)

print("A parede possui {} m², e são necessários {:.0f} litros de tinta para pintá-la." .format(a, t))