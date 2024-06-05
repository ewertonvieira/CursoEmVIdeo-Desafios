numbers = (0 ,"zero", 1 , "um", 2 ,"dois", 3 , "três", 4 , "quatro", 5 , "cinco", 6 ,"seis", 7 , "sete", 8 ,"oito", 9 ,"nove", 10 ,"dez", 11 ,"onze", 12 ,"doze", 13 ,"treze", 14 ,"quatorze", 15 , "quinze", 16 , "dezesseis", 17 ,"dezessete", 18 ,"dezoito", 19 ,"dezenove", 20 , "vinte")
while True:
    search = int(input("Digite um numero entre 0 e 20: "))
    if search <= 20 and search >= 0:
        break
    else:
        print("Tente novamente!", end = " ")
pos = numbers.index(search)
print(f"Voce digitou o numero {numbers[pos+1]}")        