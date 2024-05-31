from os import system as sy
lista_pessoas = [None] * 2; tam = len(lista_pessoas); soma = 0
idademedia = None
#
sy('cls')
for i in range(tam):
    nome = input('Informe nome: ')
    idade = input('Informe idade: ')
    op = input('Informe sexo:\nM ou m - Masculino\nF ou f - Feminino\n>> ')
    if op == 'm' or 'M':
        sexo = "MASCULINO"
    if op == 'f' or 'F':
        sexo = 'FEMININO'
    else:
        print('Erro de entrada!')
        input('Pessione qualquer tecla para sair...\n')
    sy('cls')
    # Lista: lista_pessoas esta recebendo um dicionario com 3 chaves e 3 valores: nome, idade e sexo
    lista_pessoas[i] = [{'nome' : nome, 'idade' : int(idade), 'sexo' : sexo}]
# Media de idade
for j in range(tam):
    enum = lista_pessoas[j][0]['idade']
    soma += enum
print(f'Media de idade: {soma/tam:.0f} anos')
# Qual o nome do Homem mais velho
# Quantas mulheres tem menor de 21 anos