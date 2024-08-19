from Capitulo3_Funcoes.IdentificacaoDeFuncoes import *

minhaLista=[]
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
buscarItem(minhaLista)
print("Alterando")
buscarItem(minhaLista, 20)

print("Excluindo")
print(excluirItem(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumoValores(minhaLista)