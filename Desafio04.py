algo = input('Informe "algo" >> ')
print(algo, 'é ')
if algo.isidentifier():
    print('um identificador válido')
if algo.isalnum():
    print('uma letra ou número')
if algo.isalpha():
    print('uma letra')
if algo.isascii():
    print('contém caracteres ASCII')
if algo.isdecimal():
    print('um número decimal')
if algo.isdigit():
    print('um dígito entre 0-9')
if algo.islower():
    print('uma variável que só contém letras minúsculas')
if algo.isnumeric():
    print('uma variável que só contém caracteres numéricos')
if algo.isprintable():
    print('uma variável que só contém informações imprimíveis')
if algo.isspace():
    print('uma variável que só contém espaços')
if algo.istitle():
    print('uma variável que segue o formato de título')
if algo.isupper():
    print('uma variável que só contém caracteres maiúsculos')

