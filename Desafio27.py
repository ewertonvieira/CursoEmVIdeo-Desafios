# Recebe nome completo
namef = input('Informe seu nome completo: ').strip()
# Fatia o primeiro nome
fistname = namef[:namef.find(' ')]
# Fatia o ultimo nome
lastname = namef[namef.rfind(' '):]
print(f'O primeiro nome: <{fistname}> o ultimo nome: <{lastname}>')
