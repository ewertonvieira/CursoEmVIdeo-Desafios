from os import system  as limpar
limpar('cls')
# Instancia a lista e o tamanho dela:
lista_pessoa = [0] * 4; size = len(lista_pessoa)
# Variaveis para captura de valores:
nome_masc_max = ''; idade_max = 0
# Variavel auxiliar e contador
aux = 0; count = 0

# Captura todos o dados:
for i in range(size):
    nome = input('Informe nome: ')
    idade = int(input('Informe a idade: '))
    op = int(input('Sexo: \n1 - Masculino\n2 - Feminino\n >> '))
    if op == 1:
        sexo = 'masculino'
    elif op == 2:
        sexo = 'feminino'
    else:
        input('Erro!\nSair...')
    print(30*'__')
    # Pega a media de idade do grupo, mas ainda nao foi dividido por 4:
    aux += idade
    # Pega nome do homem mais velho e sua idade:
    if sexo == 'masculino':
        if idade > idade_max:
            idade_max = idade
            nome_masc_max = nome
    # Pega o numero de mulheres menor de 20 anos:
    if sexo == 'feminino':
        if idade < 21:
            count += 1
# Imprimi tudo:
limpar('cls')
print(f'Media de idade do grupo: {aux/4:.0f}\nNome do homem mais velho\nNome: {nome_masc_max}\nIdade: {idade_max}\
    \nQuantidade de menores de 20 anos(feminino): {count}')
print(30*'__')
