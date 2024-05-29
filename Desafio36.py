def prest_mes(ano, valor_casa):
    return valor_casa/(ano * 12) # Retorna o valor das parcelas
def teste_aprov(valor_parcelas,salario_solicitante): # Testa as regras de emprestimo, retornando falso se o valor do emprestimo execeder 30% do salario
    if valor_parcelas > salario_solicitante*(30/100):
        return False
    else:
        return True
#
print('_=-='*10,'Analise para autorizar impretimo','_=-='*10)
nome_solicitante = input('INFORME SEU NOME: ').strip()
valor_casa = float(input('INFORME O VALOR DA CASA: '))
salario_solicitante = float(input('INFORME SEU SALARIO: '))
ano_pagamento = int(input('EM QUANTOS ANOS PRETENDE PAGAR: '))

prestacoes = prest_mes(ano_pagamento, valor_casa)
retorno_teste = teste_aprov(prestacoes, salario_solicitante)
print(f'''Sr(a). {nome_solicitante}, infelizmente seu empretimo nao foi aprovado! Pois o valor da parcela {prestacoes:.2f} R$ supera 30% {salario_solicitante:.2f} R$ do valor do seu salario'''if retorno_teste == False 
      else f'''Sr(a). {nome_solicitante}, sua solicitacao de emprestimo foi aprovada!''')
