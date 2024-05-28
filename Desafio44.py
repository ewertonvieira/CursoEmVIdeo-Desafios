from os import system
#
def Menu_if(valor_produto, forma_pagamento_op):
    # Dinheiro/cheque a vista:  10% de DESCONTO:
    if forma_pagamento_op == 1:
        valor_comdescon = valor_produto - (valor_produto * (10/100))
        print(f'{valor_produto} R$ com desconto de 10%(dinheiro/cheque) fica: {valor_comdescon:.2f} R$')
    # A vista CARTAO: 5% de DESCONTO:
    elif forma_pagamento_op == 2:
        valor_comdescon = valor_produto - (valor_produto * (5/100))
        print(f'{valor_produto} R$ com desconto de 5%(avista no cartao) fica: {valor_comdescon:.2f} R$')
    # 2x Cartao: preco normal | 3x ou mais: 20% de JUROS
    else:
        op = int(input('Sub/Menu:\n1 - 2x no Cartao\n2 - 3x ou mais no Cartao\n>> '))
        system('cls')
        # Sem juros ou descontos.
        if op == 1:
            print(f'{valor_produto} R$ não recebe desconto, devido forma de pagamento(2x no cartao)!')  
        # Levando em consideracao que o juros nao é progressivo.      
        else:
            valor_comjuros = valor_produto + (valor_produto * (30/100))
            print(f'{valor_produto} R$ com juros de 30% fica: {valor_comjuros}')
def Main():
    valor_produto = float(input('(Reais)Informe preco do produto:\n>> R$ '))
    forma_pagamento_op = int(input('Menu:\n1 - Dinheiro/Cheque\n2 - Cartao/A vista\n3 - Cartao/Parcelado\n>> '))
    system('cls')
    Menu_if(valor_produto, forma_pagamento_op)
# Chama a funcao Main()
if __name__ == '__main__':
    Main()