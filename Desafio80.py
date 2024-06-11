value = []
for _ in range(5):  # Itera 5 vezes para adicionar 5 números
    num = int(input('Informe um número: '))
    if not value:  # Se a lista estiver vazia, apenas adiciona o número
        value.append(num)
    else:
        inserted = False  # Variável para verificar se o número foi inserido
        for i, item in enumerate(value):  # Itera sobre os elementos e índices na lista
            if num <= item:  # Encontra o lugar certo para inserir o número mantendo a ordem crescente
                value.insert(i, num)
                inserted = True
                break
        if not inserted:  # Se não foi inserido, adiciona ao final da lista
            value.append(num)

print(value)
