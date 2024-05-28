from os import system
#
def Retorno_Apro(nome_aluno, nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media < 5:
        print(f'Media: {media} pontos\nAluno: {nome_aluno} está reprovado!')
    elif media >= 5 and media <= 6.9:
        print(f"Media: {media} pontos\nAluno: {nome_aluno} está de recuperação!")
    else:
        print(f'Media: {media} pontos\nAluno: {nome_aluno} está Aprovado!')
def Main():
    system('cls')
    nome_aluno = input('Infomre nome do aluno: ')
    nota1 = float(input('Informe nota 1: '))
    nota2 = float(input('Informe nota 2: '))
    nota3 = float(input('Informe nota 3: '))
    nota4 = float(input('Informe nota 4: '))
    system('cls')
    Retorno_Apro(nome_aluno, nota1, nota2, nota3, nota4)
# Chama primeiro metodo a ser executado
if __name__ == '__main__':
    Main()