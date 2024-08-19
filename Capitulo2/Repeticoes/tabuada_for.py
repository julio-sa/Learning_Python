tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)

for numero in range(1, 11, 1):
    print("\t", tabuada, " x ", numero, " = ", tabuada*numero)