from os import system
from datetime import datetime
ano_atual = datetime.now().year
#
def Categoria(nome, ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    # ate 9 anos: Mirim
    if idade <= 9:
        print(f'{nome} de {idade} anos está na categoria: Mirim')
    # ate 14 anos: Infantil
    elif idade <= 14:
        print(f'{nome} de {idade} anos está na categoria: Infantil')
    # ate 19 anos: Junior
    elif idade <= 19:
        print(f'{nome} de {idade} anos está na categoria: Junior')
    # ate 20 anos: Senior
    elif idade <= 20:
        print(f'{nome} de {idade} anos está na categoria: Senior')
    # superior: Master
    else:
        print(f'{nome} de {idade} anos está na categoria: Master')
def Main():
    system('cls')
    nome = input('Informe nome: ')
    ano_nascimento = int(input('Informe ano de nascimento: '))
    system('cls')
    Categoria(nome, ano_atual, ano_nascimento)
# chama Main()
if __name__ == '__main__':
    Main()
    
    