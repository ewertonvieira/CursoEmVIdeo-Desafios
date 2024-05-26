kmh = float(input('Informe sua velocidade atual(Km/h): '))
if kmh > 80.0:
    print(f'Voce foi multado em {(kmh - 80)*7} R$')