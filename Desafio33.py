lista=[0]*3
lista[0] = int(input('Informe primeiro numero: '))
lista[1] = int(input('Informe Segundo numero: '))
lista[2] = int(input('Informe Terceiro numero: '))
i = 0
while i != len(lista):
    k = 0
    while k != len(lista) - i -1:
        if lista[k] < lista[k+1]:
            lista[k], lista[k+1] = lista[k+1], lista[k]
        k += 1
    i += 1
print(f"O maior numero é {lista[0]} enquanto o menor é: {lista[2]}")