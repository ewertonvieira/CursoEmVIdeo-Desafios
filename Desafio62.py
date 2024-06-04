from os import system
def PA(a1, r, x):
    n = 0
    print(f'Primeiros {10+x} membros da progressao: ')
    while n != 10+x:
        an = a1 + (n - 1) * r
        print(f"{an}", end = " ")
        n += 1
    
a1 = int(input('Informe o valor de n(Primeiro termo): '))
r = int(input('Informe o valor de r(Razao da PA): '))
# Chama PA()
PA(a1, r, 0)

while True:
    x = int(input("\nQuer mostrar mais mebros?\n0 - Nenhum\nQuantos?(ex: 10)\n>> "))
    if x == 0:
        break
    else:
        system('cls')
        PA(a1, r, x)