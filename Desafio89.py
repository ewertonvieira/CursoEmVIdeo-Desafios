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
print('NO.      Nome        MEDIA')
print('____'*10)
for enum, aluno in enumerate(controleacademico):
    print(enum,'   ',aluno[0],' '*(15-len(aluno[0])),(aluno[1][0]+aluno[1][1])/2)
print('=-=-'*10)
while True:
    opaluno = int(input('Mostra a nosta de qual aluno separdamente?(999 para parar) '))
    print(f'Nota de {controleacademico[opaluno][0]} são: {controleacademico[opaluno][1]}')
    if opaluno == 999:
        print('FINALIZANDO...')
        break        
print('<<< VOLTE SEMPRE >>>'.center(49))