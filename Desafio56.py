from os import system as sy
lista_pessoas = [None] * 4; count = 0; soma = 0
size = len(lista_pessoas)
#
sy('cls')
for i in range(size):
    nome = str(input('Informe nome: '))
    idade = int(input('Informe idade: '))
    op = int(input('Menu:\n1 - Masculino | 2 - Femino\n>> '))
    if op == 1:
        sexo = 'masculino'
    if op == 2:
        sexo = 'feminino'
    print('-'*30)
    lista_pessoas[i] = [{"nome" : nome, "idade" : idade, "sexo" : sexo}]

sy('cls')
for j in range(0, size):
    idade = lista_pessoas[j][0]["idade"]
    soma = idade + soma
print(f'Media de idade: {soma/size:.2f} anos\n')
print('-'*30)

lista_pessoas.sort(key=lambda x: x[0]["idade"])

for jk in range(0, size):
    if lista_pessoas[jk][0]["idade"] < 21:
        count += 1
    if lista_pessoas[jk][0]["sexo"] == 'masculino':
        print(f"Nome do homem mais velho: {lista_pessoas[size-1][0]["nome"]}\n")
        print('-'*30)
        break
print(f"Mulheres menores de 21: {count}\n")
print('-'*30)
