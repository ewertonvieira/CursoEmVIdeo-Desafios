count = 0
carac = str(input('Informe uma expressao matematica: ')).replace(' ', '')
carac = carac.split()
for item in carac:
    for paren in item:
        if paren == '(':
            count += 1
        elif paren == ')':
            count -= 1
print(f'Expressão {item} valida!' if count == 0 else f'Expressão {item} invalida!')