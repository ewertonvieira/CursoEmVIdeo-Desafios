total = 0.0
count1 = 0
count = 0
nome_barato = ""  # Inicialize a variável nome_barato
menorpreco = 0.0
print("-"*60)
print("LOJA SUPER BARATAO".center(57))
print("-"*60)
while True:
    nome_produto = input("Nome do produto: ")
    preco = float(input("Valor do produto: R$ "))
    continuar = input("Deseja continuar? [S/N]: ").upper()
    if continuar == "N":
        break
    else:
        count += 1
        # Total da compra
        total += preco
        # Numero de produtos que custam mais de 1000 reais
        if preco > 1000:
            count1 += 1
        # Nome do produto mais barato
        if count == 1 or preco < menorpreco:
            nome_barato = nome_produto
            menorpreco = preco
    print("-"*60)
    print("Novo cadastro...".center(57))
    print("-"*60)

print("-"*60)
print(f"O total da compra foi R$ {total:.2f}")
print(f"Temos {count1} produto(s) custando mais de R$ 1000.00")
print(f"O produto mais barato foi '{nome_barato}' custando R$ {menorpreco:.2f}")
