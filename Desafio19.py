from random import randrange

# Randomiza o indice de uma array
def namerand():
    x = randrange(0, 3, 1)
    return x
# Instacia array via while
listnames = [0] * 4
# Add 4 nomes ao array listnames[]
i = 0
while i <= 3:
    listnames[i] = str(input(f"Informe nome >>> "))
    i += 1
# Imprime sorteado 
print(f"Nome sorteado: {listnames[namerand()]}")