name = input("Informe seu nome completo: ").strip()
# O nome de todas as letras MAICUSCULAS;
print(f'Nome caixa alta: {name.upper()}')
# O nome com todas minusculas
print(f'Nome caixa baixa: {name.lower()}')
# Quantas letras ao todo, sem contar espacos;
namenospace = name.replace(" ", "")
print ('O nome informado possui: ',len(namenospace),'Letras')
# quantas letras tem o primeiro nome;
name = name.lstrip()
fistname = name[:name.find(" ")]
print(f'Numero de letras do primeiro nome: {len(fistname)} | Primeiro nome: {fistname} ')