tupla_nome = ("Abacaxi", "Banana", "Cachorro", "Domingo", "Elefante", "Felicidade", "Girassol",
              "Harmonia", "Igreja", "Jardim", "Karate", "Limao", "Montanha", "Navio", "Ovelha",
              "Piano", "Queijo", "Rato", "Sol", "Tigre", "Uva", "Vela", "Xadrez", "Yoga", "Zebra",
              "Arco-iris", "Borboleta", "Ceu", "Dente")
for palavras in tupla_nome:
    vogais = ""
    for i in range(len(palavras)):
        if  palavras[i].lower() == 'a' or palavras[i].lower() == 'e' or \
            palavras[i].lower() == 'i' or palavras[i].lower() == 'o' or \
            palavras[i].lower() == 'u':
                vogais = palavras[i]
        print(vogais, end = " ")