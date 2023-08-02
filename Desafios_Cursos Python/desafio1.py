# Lista somente com o primeiro número primo
lista_numeros = [2]
# Inicio dos Elemntos
proximo_numero = 2

# Loop até 50
while len(lista_numeros) < 50:
    # Informando que a cada Loop deve adicionar +1 ao próxinmo número
    proximo_numero += 1
# Informção do número
    status_n = ""
# Loop para o cálculo onde o i percorre a lista e passa o elemento divisor
    for i in lista_numeros:
        quociente = proximo_numero / i
        geral = proximo_numero // i
# Caso o resto seja igual ao quociente informara para pular e para ali
        if geral == quociente:
            status_n = "pula"
            break
# Se o status do número for pula continue recomeçando o código apartir do próximo número
    if status_n == "pula":
        continue
# Caso não seja nenhuma das variações então listar o número dentro da lista
    else:
        lista_numeros.append(proximo_numero)
print(lista_numeros)


