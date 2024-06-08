total = 0.0
count1 = 0
nome_barato = ""; precobarato = 0.0
print("-"*60)
print("LOJA SUPER BARATAO".center(57))
print("-"*60)
while True:
    nomeprodu = input("Nome do produto: ")
    preco = float(input("Valor do produto: R$ "))
    continuar = input("Deseja continuar? [S/N]: ")
    continuar = continuar.upper()
    if continuar == "N":
        break
    else:
    # Total da comprar
        total += preco
    # Numero de produtos que custam mais de 1000 reais
        if preco > 1000:
            count1 += 1
    # Nome do produto mais barato
        if precobarato is None or preco < precobarato:
            precobarato = preco
            nome_barato = nomeprodu

        #
        print("-"*60)
        print("Novo cadastro...".center(57))
        print("-"*60)
print("-"*60)
print(f"O total da compra foi R$ {total}")
print(f"Temos {count1} produto custando mais de R$ 1000.00")
print(f"O produto mais barato foi a {nome_barato} custando R$ {precobarato}")