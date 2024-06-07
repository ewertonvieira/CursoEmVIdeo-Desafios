count = 0; soma = 0
while True:
    valor = int(input("Informe um valor(999 para parar): "))
    if valor == 999:
        print(f"A soma dos {count} foi {soma}")
        break
    count += 1
    soma += valor