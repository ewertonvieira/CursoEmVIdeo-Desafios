n = int(input("Informe primeiro membro da sequencia de Fibonacci: "))
if n >= 0:
    i = 0; a = 0; b = 1
    while i < n:
        a = b
        b = a + b
        print(a, end = " ")
        i += 1
else:
    print("Nao existe sequencia para esse numero")