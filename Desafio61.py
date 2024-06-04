n = 0
a1 = int(input('Informe o valor de n(Primeiro termo): '))
r = int(input('Informe o valor de r(Razao da PA): '))

print('Primeiros 10 membros da progressao: ')
while n != 10:
    an = a1 + (n - 1) * r
    print(f"{an}", end = " ")
    n += 1