namep = input('Informe seu nome: ')
namep = namep.upper()

if namep.find('SILVA') != -1:
    print(f'Nome: {namep} contem "Silva" ')
else:
    print(f'Nome: {namep} nao contem "Silva"')
    