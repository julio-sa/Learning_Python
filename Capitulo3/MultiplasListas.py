equipamentos = []
valores = []
numeroSerial = []
departamento = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    numeroSerial(int(input("Número Serial: ")))
    departamento.append((input("Departamento: ")))
    resposta = input("Digite 'S' para continuar: ").upper()

for equipamento in range(0,len(equipamentos)):
    print("Equipamento: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", numeroSerial[indice])
    print("Departamento.: ", departamento[indice])

busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
  if busca==equipamentos[indice]:
    print("Valor..: ", valores[indice])
    print("Serial.:", seriais[indice])

depreciacao = input("Digite qual equipamento passará por depreciação: ")
for indice in range(0,len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0,90
        print("Valor atualizado: ", valores[indice])

serial = input("Digite o serial do equipamento que será descartado: ")
for indice in range(0,len(equipamentos)):
    if serial == numeroSerial[indice]:
        print("O equipamento " + equipamentos[indice] + " será descartado.")
        confirmacao = input("Confirma? (Sim ou Nao)").upper()
        if confirmacao == "SIM":
            del equipamentos[indice]
            del valores[indice]
            del numeroSerial[indice]
            del departamento[indice]
            print("Equipamento descartado com sucesso")
            break

for equipamento in range(0,len(equipamentos)):
    print("Equipamento: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", numeroSerial[indice])
    print("Departamento.: ", departamento[indice])