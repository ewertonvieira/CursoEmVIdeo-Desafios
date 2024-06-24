soma = 0; somacol = 0; maior = 0
matriz = [[],[],[]]
# Captura de dados
for line in range(0, 3):
    for col in range(0, 3):
        num = int(input(f'Digite um valor para a posição[{line}, {col}]: '))
        matriz[line].append(num)
        if num % 2 == 0:
            soma += num
        if line == 1:
            if num > maior:
                maior = num
        if col == 2:
            somacol += num
# Printando matriz na tela
print('=-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[  {matriz[l][c]}  ]", end="")
    print('')
print('=-'*20)
# Estatisticas
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos da terceira coluina é {somacol}.')
print(f'O maior valor da segunda linha é {maior}.')