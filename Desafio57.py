sexo = ""
i = 0
while sexo  != "m" and sexo != "f":
    sexo = input('Menu:\nm - Marculino\nf - Feminino\n>> ').strip().lower()
    i += 1
print(f'Entrada aceita para: {sexo}')