#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
# Para ser primo --> você precisa verificar se existe algum outro numero diferente dele mesmo e de 1 que divida ele.
numero = int(input("Digite um número inteiro: "))
primo = True
i = 2
while i < numero:
    if numero % i == 0: # Se o resto da divisão de numero por i for == 0 ele não é primo
        primo = False
    i = i + 1
if primo:
    print("primo")
else:
    print("não primo")