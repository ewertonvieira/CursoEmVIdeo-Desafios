lista_produc = ("Arroz (1kg)", 5.99, "Feijão (1kg)", 3.49, "Óleo de Soja (900ml)", 4.79, "Leite (1L)", 2.99,
                "Café (500g)", 7.29, "Açúcar (1kg)", 2.19, "Sal (1kg)", 1.29, "Macarrão (500g)", 2.49,
                "Farinha de Trigo (1kg)", 3.99, "Fraldas (pacote com 50)", 25.99)
for i in range(0, len(lista_produc), 2):
    produto = lista_produc[i]
    preco = str(lista_produc[i + 1])
    print(produto, (70 - len(produto))*".","R$", preco.center(1)) 
    # Removendo o numero de caracteres de 'produto' do numero de linhas 