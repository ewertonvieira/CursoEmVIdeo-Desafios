numlist = [[], []]
for i in range(1, 8):
    numb = int(input(f'Informe o {i}º valor: '))
    if numb % 2 == 0:
        numlist[0].append(numb)
    else:
        numlist[1].append(numb)
print('-='*21)
print(f'Os valores pares digitados foram: {sorted(numlist[0])}\nOs valores impares digitados foram: {sorted(numlist[1])}')