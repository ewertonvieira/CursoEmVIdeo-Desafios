count = 0
carac = str(input('Informe uma expressao matematica: ')).replace(' ', '')
for paren in carac:
    if paren == '(':
        count += 1
    elif paren == ')':
        count -= 1
print(f'Expressão {carac} valida!' if count == 0 else f'Expressão {carac} invalida!')