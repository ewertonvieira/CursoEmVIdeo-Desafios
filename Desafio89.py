controleacademico = []

while True:
    print('=-=-'*10)
    nome = input('Digite um nome: ').title()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    controleacademico.append([nome,[nota1, nota2]])
    op = input('>> Quer continuar!?[S/N]: ').upper()
    if op in ['N']:
        break
print('****'*10)
print('NO.  Nome     MEDIA')
print('____'*10)
for enum, aluno in enumerate(controleacademico):
    print(enum,'  ',aluno[0],'    ',(aluno[1][0]+aluno[1][1])/2)