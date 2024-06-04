
def main():
    soma = 0; div = 0; mult = 0; sub = 0
    while True:
        op = int(input('Menu:\n1 - Soma\n2 - Divisao\n3 - Multiplicacao\n4 - Subtracao\n>> '))
        num1 = float(input('Informe primeiro numero: '))
        num2 = float(input('Informe segundo numero: '))
        
        if op == 1:
            print(f"Resposta: {num1 + num2}")
            soma = 1
        elif op == 2:
            print(f"Resposta: {num1 / num2}")
            div = 2
        elif op == 3:
            print(f"Resposta: {num1 * num2}")
            mult = 3
        else:
            print(f"Resposta: {num1 - num2}")
            sub = 4 

        if (soma == 1) and (div == 2) and (mult == 3) and (sub == 4):
            break
        
if __name__ == "__main__":
    main()