print('-'*12,'Teste-Palidromo','-'*12)
# Ler frase ou palavra
frase = input('Informe uma frase:\n>> ')
pali = frase[::-1]
if frase.title() == pali.title():
    print(f'Essa frase é um palidromo: "{frase}" e invertida: "{pali}"')
else:
    print(f'A frase nao se trata de um palidromo: "{frase}" e invertida "{frase[:-1]}" é completamente diferente!')A