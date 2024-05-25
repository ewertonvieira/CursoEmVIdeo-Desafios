city = input('Informe nome da cidade em que mora: ')
city = city.upper()

# starswith procura se uma string comeca com determinado parametro:
if city.startswith('SANTO') == True:
    print(f'Nome da cidade: {city} se inicia com "Santo"')
elif city.startswith('SANTO') == False:
    print(f'Nome da cidade: {city} nao se inicia com "Santo"')