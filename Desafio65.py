op = ""; count = 0; soma = 0; num = 0
auxmax = None
auxmin = None

while True:
    num = int(input("Numero: "))
    #
    soma += num
    count += 1
    #
    if auxmin is None or num < auxmin:
        auxmin = num
    elif auxmax is None or num > auxmax:
        auxmax = num
    # Finaliza loop caso escolha = n
    op = input("Deseja continuar? (S/N)").lower()
    if op == 'n':
        break
print(f"Media: {soma/count:.0f} | Maior: {auxmax} Menor: {auxmin}")