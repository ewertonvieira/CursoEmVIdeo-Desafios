from datetime import datetime

def Alistamento(ano_atual, ano_nascimento, nome_user):
    idade = ano_nascimento - ano_atual
    if idade < 16:
        print(f'{nome_user} não pode se alistar, devido sua idade: {idade} anos ser inferior 16.')
    elif idade > 18:
        print(f'{nome_user} não pode se alistar, pois sua idade: {idade} anos ser superir a 18.')
    else:
        print(f'{nome_user} pode e deve se alistar, pois sua idade: {idade} anos permite o alistamento.')
ano_atual = datetime.now().year
nome_user = input('Informe seu nome:\n>> ').strip().title()
nome_user = ' '.join(nome_user.split())
ano_nascimento = int(input('Informe ano em que nasceu:\n>> '))
Alistamento(ano_nascimento, ano_atual, nome_user)