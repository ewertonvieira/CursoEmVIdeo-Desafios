nome = input('Nome: ')
media = float(input(f'Media de {nome}: '))
while media < 0:
    media = float(input(f'Media invalida, tente novamente...\nMedia de {nome}: '))

if media >= 7:
    dic_alunos = {'Nome': nome, 'Media': media, 'Situacao': 'Aprovado(a)'}
elif media < 7:
    dic_alunos = {'Nome': nome, 'Media': media, 'Situacao': 'Reprovado(a)'}
    
print(f'O nome é igual a {dic_alunos["Nome"]}\nA media é igual a {dic_alunos["Media"]}\nSituação é igual a {dic_alunos["Situacao"]}')