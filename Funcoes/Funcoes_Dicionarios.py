def perguntar():
    resposta = input("O que deseja realizar?"+
                  "<I> - Para Inserir um usuário"+
                  "<P> - Para Pesquisar um usuário"+
                  "<E> - Para Excluir um usuário"+
                  "<L> - Para Listar um usuário\n").upper()
    return resposta
def inserir(dicionario):
    dicionario[input("Digite o código de lançamento: ").upper()] = [input("Digite o login: ").upper(),
                                                     input("Digite o nome: ").upper(),
                                                     input("Digite a data de acesso: "),
                                                     input("Qual o horário de acesso: "),
                                                     input("Qual a estação acessada: ").upper()]
def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def pesquisarIp(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Digite os dois primeiros octetos..: " + lista[1])
        print("Digite os dois últimos octetos....: " + lista[2])
def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Usuário excluído.")
def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)

def monitorarRede(dicionario, chave):
    resposta = "S"
    while resposta == "S":
        for chave, dado in dicionario.items():
            if dicionario[0][1] == chave:
                print(chave[0][1] + "." + chave[1][1] + "\tLogin...: " + dado[0], "\n")
        resposta == input("Digite <S> para verificar uma nova rede: ").upper()

def monitorarAcessos(dicionario, chave):
    resposta = "S"
    while resposta == "S":
        for chave, dado in dicionario.items():
            if chave[1][1] == chave:
                print(chave[0][1] + "." + chave[1][1] + "\tLogin...: " + dado[0], "\n")
            resposta == input("Digite <S> para verificar uma nova rede: ").upper()