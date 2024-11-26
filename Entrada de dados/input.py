#Entrada de Dados --> pede para o usuário informar um dado.
"""
nome = input ("Qual seu nome ?: ")
print ("Bom dia !!! " ,nome)
"""
#Caso queira realizar alguma conta com números inteiros(int) ou flutuantes(float)
peso_str = input("Qual seu peso ?: ") #O dado vem em formato str(texto)
altura_str = input("Qual sua altura ?: ") #O dado vem em formato str(texto)
peso =float(peso_str) # Utilizando o float na frente da operação você transforma a string(str) em um número Flutuante(float)
altura = float(altura_str) # Utilizando o float na frente da operação você transforma a string(str) em um número Flutuante(float)
imc = (peso / (altura ** 2)) #Lembrando, caso queira um resultado inteiro, é só utilizar o int --> imc = int((peso / (altura ** 2)))
print(imc)