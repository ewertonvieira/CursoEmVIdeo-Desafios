count = 0
found = False
xpr = str(input('Informe uma expressao matematica: ')).replace(' ', '')
xpr = xpr.split()
for char in xpr[0]:
    if char == '(':
        found = True
        count += 1
    elif char == ')' and found == True:
        count -= 1
        found = False
print('Operacao valida' if count == 0 else 'Operacao Invalida')