from datetime import datetime, timedelta
data_aniversario = [None] * 7;
data_now = datetime.now()
cont_21 = 0; cont_min = 0
#
print('--'*30)
print('Informe sua data de aniversario no formato (dd - mm - aa): \n')
# Inserindo as capturas de datas em uma lista de 7 espacos
for i in range(len(data_aniversario)):
    dia = int(input('Dia: '))
    mes = int(input('Mes: '))
    ano = int(input('Ano: '))
    print('--'*20)
    data_aniversario[i] =  datetime(day=dia, month=mes, year=ano)
# Percorrendo a lista de datas
for j in range(len(data_aniversario)):
    # Pegando a diferenca de dias entre a data atual e a data de aniversario informanda anteriormente
    dias_bith = (data_now - data_aniversario[j]).days
    # Comparando a diferenca de dias anterior a o numero de dias que 21 anos tem
    if dias_bith >= timedelta(21*365).days:
        cont_21 += 1
    else:
        cont_min += 1
print("Numero de pessoas maiores de 21 anos e menores presente na lista:")
print(f"Maiores: {cont_21}\nMenores: {cont_min}")