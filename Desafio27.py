# Recebe nome completo
namef = input('Informe seu nome completo: ')
# Fatia o primeiro nome
fistname = namef[:namef.find(' ')]
# Fatia o ultimo nome
lastname = namef[namef.rfind(' '):]
print(f'O primeiro nome: <{fistname.strip()}> o ultimo nome: <{lastname.strip()}>')
