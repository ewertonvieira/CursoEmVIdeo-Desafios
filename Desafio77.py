tupla_nome = ("Abacaxi", "Banana", "Cachorro", "Domingo", "Elefante", "Felicidade", "Girassol",
              "Harmonia", "Igreja", "Jardim", "Karate", "Limao", "Montanha", "Navio", "Ovelha",
              "Piano", "Queijo", "Rato", "Sol", "Tigre", "Uva", "Vela", "Xadrez", "Yoga", "Zebra",
              "Arco-iris", "Borboleta", "Ceu", "Dente")
for palavras in tupla_nome:
    print(f"\n{palavras}: ",end="")
    vogais = ""
    for letras in palavras:
        if letras.lower() in "aeiou":
            if letras not in vogais:
                vogais = letras
            print(f"{vogais}", end="")