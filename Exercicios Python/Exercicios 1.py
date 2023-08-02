x = -6

if x == str:
    print('Não e um número')

elif x > 0:
    print('Número Postivo')
elif x < 0:
    print('Número Negativo')
elif x == 0:
    print('Zero')


# EXERCICIO 2
lista = [1, 2, 3, 4, 5]
valores = ['a', 'b', 'c', 'd', 'f']
new = []

for i in range(5):
    new.append(lista[i])
    new.append(valores[i])
print(new)

# Exercicio 3

x = 5
fact_x = 1

if type (x) is int:
    while x > 0:
        fact_x *= x
        x -= 1
    print(fact_x)

