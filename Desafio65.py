op = ""; count = 0; soma = 0; auxmax = 0; auxmin = 0; num = 0
if num < auxmin:
    auxmin = num
elif num > auxmax:
    auxmax = num

while True:
    num = int(input("Numero: "))
    #
    soma += num
    count += 1
    #
    if num < auxmin:
        auxmin = num
    elif num > auxmax:
        auxmax = num
    # Finaliza loop caso escolha = n
    op = input("Deseja continuar? (S/N)").lower()
    if op == 'n':
        break
print(f"Media: {soma/count} | Maior: {auxmax} Menor: {auxmin}")