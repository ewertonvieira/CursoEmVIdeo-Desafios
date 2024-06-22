pessoas = []; maispesadas = []; maisleves = []
count = 0

while True:
    print('*'*20)
    nome = input('INFORME NOME: ')
    peso = float(input('INFORME NOME(Kg): '))
    pessoas.append([nome, peso])
    op = str(input('Deseja continuar?[S/N]... ')).upper()
    if op in "N":
        break
pesos = [pessoa[1] for pessoa in pessoas]
pesomax = max(pesos)
pesomin = min(pesos)

for pessoa in pessoas:
    if pessoa[1] == pesomax:
        maispesadas.append(pessoa[:])
    if pessoa[1] == pesomin:
        maisleves.append(pessoa[:])
print(maispesadas)
print(maisleves)
print('*'*60)
print(f'Ao todo, voce cadastrou {len(pessoas)}')