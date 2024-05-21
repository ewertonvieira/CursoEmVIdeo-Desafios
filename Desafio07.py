import os

nota1 = float(input('Informe a primeira nota >>> '))
nota2 = float(input('Informe a segunda nota >>> '))
nota3 = float(input('Informe a terceira nota >>> '))
nota4 = float(input('Informe a quarta nota >>> '))
os.system('cls')

media = (nota1 + nota2 + nota3 + nota4)/4
if media >= 7:
    print(f'Aluno aprovado! com a media {media:.1f}')
if (media < 7) and (media >= 5):
    print(f'Aluno de recuperacao! com a media {media:.1f}')
else:
    print(f'Aluno reprovado! Com a media: {media:.1f}')
