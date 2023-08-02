# Pegar valores
alg_romanos = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
print(alg_romanos['III'])

# Remove valor especifico "Pop"
alg_romanos = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
print(alg_romanos.pop('IV'))
print(alg_romanos)

# Tranforma os valores em tuplas "items"
alg_romanos = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
print(list(alg_romanos.items()))

# Retorna valroes chaves  'Keys'
alg_romanos = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
print(alg_romanos.keys())
print(list(alg_romanos.keys()))

# Retorna os valores
alg_romanos = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
print(alg_romanos.values())
print(list(alg_romanos.values()))

# Recebe o valor atraves de uma chave "get"
alg_romanos = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
print(alg_romanos.get('II'))
