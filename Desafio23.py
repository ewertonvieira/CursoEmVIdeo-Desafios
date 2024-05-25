from os import system

num = int(input('(Entre 0 e 9999)INFORME NUMERO: '))
if num < 0 or num > 9999:
    input("Entrada invalida!\nPressione qualquer tecla para sair do programa!")
else:
    nums = str(num)
    match len(nums):
        case 1:
            print(f'Unidade: {nums[0]}')
        case 2:
            print(f'Unidade: {nums[0]}\nDezena: {nums[1]}')
        case 3:
            print(f'Unidade: {nums[2]}\nDezena: {nums[1]}\nCentenas: {nums[0]}')
        case 4:
            print(f'Unidade: {nums[3]}\nDezena: {nums[2]}\nCentenas: {nums[1]}\nMilhar: {nums[0]}')