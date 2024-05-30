soma = 0
num = int(input('INFORME UM NUMERO: '))
for num in range(0, num + 1):
    if num % 2 == 0:
        soma += num
print(f"Soma dos numeros pares no intervalo de 0 a '{num}'... {soma}")