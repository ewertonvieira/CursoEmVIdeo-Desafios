lista = [0] * 4
size = len(lista)

for i in range(size):
    lista[i] = int(input(f"Digite um valor inteiro para a posição [{i}]: "))

maiorvalor = max(lista)
menorvalor = min(lista)

print(f"O maior valor digitado foi {maiorvalor} e os espaços", end=" ")

for j, valor in enumerate(lista):
    if valor == maiorvalor:
        print(j, end="... ")

print(f"\nO menor valor digitado foi {menorvalor} e os espaços", end=" ")

for k, valor in enumerate(lista):
    if valor == menorvalor:
        print(k, end="... ")
