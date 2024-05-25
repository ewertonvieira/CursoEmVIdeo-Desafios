frase = input('Informe uma frase: ').strip()
frase = frase.upper()
# Quantas vezes aparece a letra A:
print(f'A letra "a" aparece: {frase.count('A')} vezes')
# Em qual posicao a letra a aparece pela primeira vez
print(f'A letra "a" aparece primeiro na prosicao: {frase.find('A')}')
# Em qual posicao a letra a aparece pela ultima vez
print(f'A letra "a" aparece pela ultima vez na posicao: {frase.rfind('A')}')