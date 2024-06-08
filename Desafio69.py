idademax = 0
countm = 0
countf = 0

while True:
    print("_"*30)
    idade = int(input("Idade: "))
    sexo = input("Sexo?[M/F] ").upper()
    while sexo not in ["M", "F"]:
        print("Valor inválido. Informe [M/F]")
        sexo = input("Sexo?[M/F] ").upper()

    if idade > 18:
        idademax += 1

    if sexo == "M":
        countm += 1
    else:
        if idade < 20:
            countf += 1

    op = input("Quer continuar? [S/N]").upper()
    while op not in ["S", "N"]:
        print("Valor inválido. Informe [S/N]")
        op = input("Quer continuar? [S/N]").upper()

    if op == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {idademax}")
print(f"Ao todo temos {countm} homens cadastrados.")
print(f"E temos {countf} mulheres com menos de 20 anos.")
