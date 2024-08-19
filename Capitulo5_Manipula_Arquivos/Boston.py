with open("economic-indicators.csv","r") as boston:
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    menor_taxa_ocupacao = float('inf')
    maior_taxa_ocupacao = 0
    menor_taxa_desemprego = float('inf')
    maior_taxa_desemprego = 0
    ano_usuario = input("Qual ano deseja pesquisar? ")

    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        total_voos = total_voos + float(lista[3])
        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        if ano_usuario == lista[0]:
            total_passageiros = total_passageiros + float(lista[2])
            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]
            if float(lista[4]) > float(maior_taxa_ocupacao):
                maior_taxa_ocupacao = lista[4]
                mes_maior_ocupacao = lista[1]
            if float(lista[4]) < float(menor_taxa_ocupacao):
                menor_taxa_ocupacao = lista[4]
                mes_menor_ocupacao = lista[1]
            if float(lista[7]) > float(maior_taxa_desemprego):
                maior_taxa_desemprego = lista[7]
                mes_maior_desemprego = lista[1]
            if float(lista[7]) < float(menor_taxa_desemprego):
                menor_taxa_desemprego = lista[7]
                mes_menor_desemprego = lista[7]

    print("O total de voos é: ", total_voos)
    print("O mês/ano de maior movimento no aeroporto foi: ", str(mes),"/",str(ano))
    print("O total de passageiros do ano ", ano_usuario, "foi de ", total_passageiros)
    print("O mês do ano ", ano_usuario, "com maior média para diária de hotel foi ", mes_maior_diaria)
    print("A maior taxa de ocupação dos hotéis no ano foi ", float(maior_taxa_ocupacao) * 100, "%", "em", mes, ano_usuario)
    print("A menor taxa de ocupação dos hotéis no ano foi ", float(menor_taxa_ocupacao) * 100, "%", "em", mes, ano_usuario)
    print("A maior taxa de desemprego no ano foi ", float(maior_taxa_desemprego) * 100, "%", "em", mes, ano_usuario)
    print("A menor taxa de desemprego no ano foi ", float(menor_taxa_desemprego) * 100, "%", "em", mes, ano_usuario)
