from random import sample

# Inicializa os arrays de tamanho 3
list = [0] * 4
listorder = [0] * 4
size = len(list)

# Função que retorna uma lista de índices aleatórios únicos
def sorteio(size):
    return sample(range(size), size)

# Coleta os nomes dos líderes dos grupos
i = 0
while i < size:
    list[i] = input("Informe nome do líder de grupo >>> ")
    i += 1

# Gera uma lista de índices aleatórios únicos
indices = sorteio(size)

# Ordena a lista de nomes de acordo com os índices aleatórios
k = 0
while k < size:
    listorder[k] = list[indices[k]]
    k += 1

# Printa os nomes ordenados via sorteio
print("Nomes ordenados via sorteio:", listorder)
