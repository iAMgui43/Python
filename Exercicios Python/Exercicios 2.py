# Dada a lista ['P','A', 'Y', 'A', 'T', 'A', 'H','O', 'N']
# conte o número de variáveis 'A' e utilize um loop para remover todos os 'A' excedente.

Lista_1 = ['P', 'A', 'Y', 'A', 'T', 'A', 'H', 'O', 'N']

Numero_A = Lista_1.count('A')

for i in enumerate(Lista_1):
    letras = i[1]

    if letras == 'A':
        Lista_1.pop(i[0])

print(Lista_1)


#Exercicio 2 
#Utilizando somente uma linha de programação, crie uma lista que contenha os números impares de 1 a 51.

lista_impares = [(i*2+1) for i in range(26)]
print(lista_impares) 

f_x = lambda x:(x*2+1)
lista_impares_2 = [f_x(x) for x in range(26)]
print(lista_impares_2)

#Exercicio 3
#Crie um dicionário que correlacione as seguintes listas:
#valores = [1,2,3,4,5]
#keys = ['a','b','c', 'd','e']
#Utilize um loop.

valores = [1,2,3,4,5]
keys = ['a','b','c', 'd','e']

dict_1 = {}

for i in range(5):
    dict_1[keys[i]] = valores[i]
print(dict_1)

#Exercicio 4
#A partir do dicionário criado no exercício anterior, recrie as listas keys e valores.

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(list(dict.values()))
print(list(dict.keys()))


