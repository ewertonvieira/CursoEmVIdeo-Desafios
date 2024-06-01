dist = float(input("Informe a distancia percorrida em (km): "))
print(f'Valor da passagem: {dist*0.50} R$'if dist<=200 else f'Valor da passagem: {dist*0.45} R$ ' )