listanum = []
for _ in range(5):
    num = int(input('Informe um numero: '))
    if not listanum: # add num ao inicio da lista se a listanum estiver fazia
        listanum.append(num)
    else:
        inserido = False # instancia inserido.
        for i, item in enumerate(listanum):
            if item >= num:
                listanum.insert(i, num)
                inserido = True # se o valor foi insetido o valor se torna True
        if inserido == False:
            listanum.append(num)
print(listanum)