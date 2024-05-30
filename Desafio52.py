num = int(input('Informe o numero a ser testado: '))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f'{num} nao é primo')
            break
    else:
        print(f'{num} é primo.')
else:
    print(f"{num} nao é primo.")