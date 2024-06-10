lista = [int] * 4
size = len(lista)

for i in range(size):
    lista[i] = int(input(f"Digite um valor inteiro para a posicao [{i}]: "))
maior = max(lista)
menor = min(lista)

maiorl = []; menorl = []
for k in range(size):
    if maior == lista[k]:
        maiorl.append(k)
        maiorf = '... '.join(map(str, str(maiorl)))
    if menor == lista[k]:
        menorl.append(k)
        menorf = '... '.join(map(str, str(menorl)))
print(f'Voce digitou: {lista}')
print(f"O maior número digitado: {maior} na(s) posição(ões) {maiorf}")
print(f"O menor número digitado foi {menor} na(s) posição(ões) {menorf}")
