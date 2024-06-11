valores = []
while True:
    num = int(input('Digite um numero: '))
    if num not in valores:
        print(f'Valor {num} adicionado com sucesso...')
        valores.append(num)
    else:
        print(f'Valor {num} duplicado! Nao vou adicionar!')
    op = input('Deseja continuar?[S/N] ').upper()
    if op == 'N':
        break
    else:
        pass

valores = sorted(valores)
print(' - '.join(map(str, valores)))