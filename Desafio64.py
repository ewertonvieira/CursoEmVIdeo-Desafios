aux = 0; count = 0
while True:  
    numero = int(input("Numero: "))     
    if numero == 999:
        break
    aux += numero
    count += 1
print(f"Countador: {count} | Soma: {aux}")