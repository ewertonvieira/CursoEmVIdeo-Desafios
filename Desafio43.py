from os import system
#
def t_imc(nome, altura, peso):
    imc = peso / (altura*altura) # Define o imc
    # Abaixo de 18.5: Abaixo do peso
    if imc < 18.5:
        print(f'Sr(a). {nome}, seu imc {imc:.2f} é preocupante pois esta abaixo do peso ideal.')
    # Entre 18.5 e 25: Peso ideal
    elif imc > 18.5 and imc < 25:
        print(f'Sr(a). {nome}, seu imc {imc:.2f} é o ideal! Parabens!')
    # 25 ate 30: Sobrepeso
    elif imc >= 25 and imc < 30:
        print(f'Sr(a). {nome}, seu imc {imc:.2f} indica sobrepeso.')
    # 30 e 40: Obesidade
    elif imc >= 30 and imc < 40:
        print(f'Sr(a). {nome}, seu imc {imc:.2f} indica obesidade.')
    # Acima de 40: Obsidade morbida
    else:
        print(f'Sr(a). {nome}, seu imc {imc:.2f} indica obesidade morbida. Isso é preocupante!')

def Main():
    system('cls')
    nome = str(input('Informe seu nome: ')).strip().title() # Remove espacos da direito e esquerda da string, capitaliza a primeira letra de cada string deixando maisculas
    nome = ' '.join(nome.split()) # Transforma nome em uma lista e join transforma novamente para um string, garantindo apenas 1 espaco entre as palavras
    altura = float(input('(ex: 1.80 para 1.80m)Informe sua altura em metros: '))
    peso = float(input('(ex: 60.0 para 60kg)Informe seu peso em kg: '))
    system('cls')
    t_imc(nome, altura, peso)
    # Chama a funcao Main()
if __name__ == '__main__':
    Main()