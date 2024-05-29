from random import randint
from time import sleep
from os import system

def Esc_maquina():
    escolha = randint(1, 3)  # Seleciona um número entre 1 e 3
    if escolha == 1:
        return 'pedra'
    elif escolha == 2:
        return 'tesoura'
    elif escolha == 3:
        return 'papel'

def Esc_usuario(escolha_usuario):
    if escolha_usuario == 1:
        return 'pedra'
    elif escolha_usuario == 2:
        return 'tesoura'
    elif escolha_usuario == 3:
        return 'papel'
    else:
        return 'Escolha inválida!'

def Vencedor(op_usuario, op_maquina):
    if op_usuario == op_maquina:
        print(f'Tivemos um empate entre você (Usuário) com {op_usuario} e a máquina (PC) com {op_maquina}')
    elif (op_usuario == 'pedra' and op_maquina == 'tesoura') or \
         (op_usuario == 'tesoura' and op_maquina == 'papel') or \
         (op_usuario == 'papel' and op_maquina == 'pedra'):
        print(f'Você (Usuário) vence com {op_usuario} e a máquina (PC) perde com {op_maquina}')
    else:
        print(f'A máquina (PC) vence com {op_maquina} e você (Usuário) perde com {op_usuario}')

def Main():
    system('cls')
    print('---' * 9, 'Joquempo', '---' * 9)
    print('A máquina está escolhendo entre pedra, tesoura e papel...')
    # Captura esc_maquina
    esc_maquina = Esc_maquina()
    sleep(4)
    print('Pronto! A máquina já escolheu!!!')
    print('-'* 64)
    # Escolha do usuario
    print('Agora sua vez!')
    print('Menu de opções:\n1 - Pedra\n2 - Tesoura\n3 - Papel')
    esc_usuario = int(input('Qual sua escolha?\n>> '))
    # Captura esc_maquiina de Esc_usuario(esc_maquina)
    esc_usuario = Esc_usuario(esc_usuario)
    if esc_usuario == 'Escolha inválida!':
        input('Escolha invalida!!\nPressione uma tecla para sair...')
    # Chama Vencedor
    Vencedor(esc_usuario, esc_maquina)

if __name__ == '__main__':
    Main()