payment = float(input('INFORME O SALARIO ATUAL A SER REAJUSTADO EM "15%" >>> R$ '))
print(f'O FUNCIONARIO QUE RECEBIA R$ {payment:.2f}\nCOM 15% DE REAJUSTE, PASSA A RECEBER R$ {payment + (payment * (15/100)):.2f}')