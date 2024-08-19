nivelAcesso = input("Digite o nível de acesso (ADM, USR ou GUEST): ").upper()
if nivelAcesso=="ADM" or nivelAcesso=="USR":
    genero = input("Digite o gênero(Masculino/Feminino): ").upper()
    if nivelAcesso=="ADM":
        if genero=="MASCULINO":
            print("Olá administrador!")
        elif genero=="FEMININO":
            print("Olá administradora!")
        else:
            print("Digite um gênero biológico válido. Masculino ou Feminino")
    else:
        if genero == "MASCULINO":
            print("Olá usuário!")
        elif genero == "FEMININO":
            print("Olá usuária!")
        else:
            print("Digite um gênero biológico válido. Masculino ou Feminino")
elif nivelAcesso=="GUEST":
    print("Olá visitante!")
else:
    print("Olá desconhecido.")
