product = float(input('INFORME O VALOR DO PRODUTO QUE DESEJA CALCULAR O DESCONTO DE 5% >>> R$ '))
print(f'O PRODUTO DE VALOR R$ {product:.2f} com desconto aplicado de "5%" é R$ {product - (product * (5/100)):.2f}')