salario = float(input('Informe seu salario atual R$: '))
print(f'Aumento salario: {((12/100)*salario)+salario} R$' if salario > 1250 else f'Aumento salarial: {((15/100)*salario)+salario} R$')