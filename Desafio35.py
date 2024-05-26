r1 = float(input('Informe valor da primeira reta: '))
r2 = float(input('Informe valor da segunda reta: '))
r3 = float(input('Informe valor da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'primeira reta: {r1}, a segunda: {r2} e a terceira: {r3} podem formar um triangulo!')
else:
    print(f'primeira reta: {r1}, a segunda: {r2} e a terceira: {r3} nao podem formar um triangulo!')