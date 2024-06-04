from math import factorial

fat = 1; res = 0
num = int(input("Informe numero para fatorial: "))
if num < 0:
    print("Numero negativo nao tem fatorial!")
elif num % 2 != 0:
    i = 1
    while i <= num:
        fat *= i
        i += 1
print(fat)
        