#range
Lista_quadrado = []

for quadrado in range(5):
    Lista_quadrado.append(quadrado**2)
print(Lista_quadrado)

#List
a = list(range(12))
print(a)

#lambda || Map
a = [2, 3, 4, 5, 6]
f = lambda x:x**2
b = list(map(f,a))
print(b)

#Loop || range
quadrado_2 = [x** 2 for x in range(10)]
print(quadrado_2)