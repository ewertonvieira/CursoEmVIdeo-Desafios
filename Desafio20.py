from random import sample
# Instancia o array list
list = [0] * 4
list_o = [0] * 4
size = len(list)

i = 0
while i != size:
    list[i] = input(f"Informe nome {i}: ")
    i += 1
print(sample(list, size))

