from random import randint

print("_-"*40)
print("VAMOS JOGAR PAR OU IMPAR!".center(75))
print("_-"*40)

valor = int(input("Diga um valor: "))
parimpar = input("Par ou Impar? [P/I] ").upper()

if parimpar != "I" and parimpar != "P":
    print("Erro. PROGRAMA ENCERRADO...")
else:
    valormaquina = randint(1, 30)
    print(f"A máquina escolheu o valor {valormaquina}")
    soma = valor + valormaquina
    resultado = "Par" if soma % 2 == 0 else "Ímpar"
    
    print(f"A soma dos valores é {soma} ({resultado})")
    
    if (parimpar == "P" and soma % 2 == 0) or (parimpar == "I" and soma % 2 != 0):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
