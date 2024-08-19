from Funcoes.Funcoes_Dicionarios import *

ips = {}
resp = "S"
bytesRede = []
bytesId = []
while resp == "S":
    bytesRede.append(input("Digite os dois primeiros octetos do IP: "))
    bytesId.append(input("Digite os dois últimos octetos do IP: "))
    resp = input("Digite <S> para adicionar um novo IP: ").upper()

tuplaRede = list(enumerate(bytesRede))
tuplaId = list(enumerate(bytesId))

for chave in range(0, len(tuplaRede)):
    print("Endereço de IP da rede...: ", tuplaRede[chave][1] +"."+ tuplaId[chave][1])
    ips[tuplaRede[chave],tuplaId[chave]] = [input("Digite o login: ").upper(), input("Digite o nível de acesso: ").upper()]

for chave, dado in ips.items():
    print("Endereço de IP...: ", chave[0][1] +"."+ chave[1][1])
    print("Login de acesso..: ", dado[0])
    print("Nível de Acesso..: ", dado[1])

#Verificando as máquinas que estão presentes na rede
pesquisa = input("Digite os dois primeiros octetos da rede que deseja monitorar...: ")
print("Exibindo máquinas que acessaram a rede: \n")
monitorarRede(ips, pesquisa)

#Verificando as redes acessadas por uma máquina
pesquisa = input("Digite os dois últimos octetos da máquina que deseja monitorar...: ")
print("Exibindo redes acessadas pelo usuário: " + dado[0] + "\n")
monitorarAcessos(ips, pesquisa)