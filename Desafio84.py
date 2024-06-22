pessoas = []; maispesadas = []; maisleves = []

while True:
    print('*'*27)
    nome = input('INFORME NOME: ')
    peso = float(input('INFORME NOME(Kg): '))
    pessoas.append([nome, peso])
    op = str(input('Deseja continuar?[S/N]... ')).upper()
    if op in "N":
        break
# Captura o mair valor peso na lista pessoas
pesomax = max([peso[1] for peso in pessoas])
pesomin = max([peso[1] for peso in pessoas])
# Captura os iguais a pesso max e min na lista pessoas
for pessoa in pessoas:
    if pessoa[1] == pesomax:
        maispesadas.append(pessoa)
    if pessoa[1] == pesomin:
        maisleves.append(pessoa)
# Captura os nomes das pessoas mais pesadas e leves
pessoamax = [pmax[0] for pmax in maispesadas]
pessoamin = [pmin[0] for pmin in maisleves]
# Printa estatisticas formatadas
print('_-_'*25)
print(f'Numero de cadastros {len(pessoas)}')
print(f'Maior peso {pesomax} kg, pessoas mais pesadas {', '.join(pessoamax)}')
print(f'Menor peso {pesomin} kg, pessoas mais leves {', '.join(pessoamin)}')