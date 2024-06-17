num = []; count = 0
verifica = False
while True:
    num1 = int(input('Informe um numero: '))
    num.append(num1)
    count += 1
    if num1 == 5:
        verifica = True
    op = input('Deseja parar a execucao...[S para parar]').upper().strip()
    if op in ['S']:
        break
print(f'Quantidade de numeros digitados: {count}') # Qunatidade de numeros digitados

num = sorted(num, reverse=True)
print(', '.join(map(str, num))) # Lista em ordem inversa

print(f'O numero 5 foi digitado'if verifica == True else 'O numero 5 não foi digitado') # Confirma ou nao de numero 5 foi digitado