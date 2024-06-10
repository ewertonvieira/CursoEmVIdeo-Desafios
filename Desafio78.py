lista = [int] * 4
size = len(lista)

for i in range(size):
    lista[i] = int(input(f"Digite um valor inteiro para a posicao [{i}]: "))
maior = max(lista)
menor = min(lista)

maiorl = []; menorl = []
for k in lista:
    if maiorl >= lista:
        maiorl.append(k)
    if menorl <= lista:
        menorl.append(k)
print(f'Voce digitou: {lista}')
print(f"O maior número digitado: {maior} na(s) posição(ões) { maiorl}")
print(f"O menor número digitado foi {menor} na(s) posição(ões) {menorl}")
