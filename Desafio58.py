from random import randint
from time import sleep
from os import system as clear

def Vencedor(op_maquina, op_user):
    if op_maquina == op_user: 
        return "Empate", 1
    elif (op_user == "pedra" and op_maquina == "tesoura") or\
            (op_user == "tesoura" and op_maquina == "papel") or\
            (op_user == "papel" and op_maquina == "pedra"):
            return "Vitoria", 2
    else:
            return "Derrota, vitoria da Maquina", 3
    
def Maquina(op_maquina):
    if op_maquina == 1:
        op_maquina = "pedra"
    elif op_maquina == 2:
        op_maquina = "papel"
    else:
        op_maquina = "tesoura"
    return op_maquina
                
def Main():
    while True:
        clear('cls')
        # Escolha maquina
        print("A mquaina esta escolhendo entre pedra, papel e tesoura.\nAguaede...")
        sleep(2)
        op_maquina = randint(1, 3)
        maquina = Maquina(op_maquina)
        # Escolha Usuario
        print("Agora é sua vez!\nMenu:")
        op_user = int(input("1 - Pedra\n2 - Papel\n3 - Tesoura\n>> "))
        if op_user == 1:
            op_user = "pedra"
        elif op_user == 2:
            op_user = "papel"
        else:
            op_user = "tesoura"
        # Chama Vencedor()
        mensagem, codigo = Vencedor(maquina, op_user)
        print(f"{mensagem} com as escolhas:\nMaquina: {maquina}\nUsuario: {op_user}")
        sleep(5)
        if codigo == 2:
            break
# Chama a funcao Main()
if __name__ == "__main__":
    Main()