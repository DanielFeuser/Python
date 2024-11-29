# Faça um programa que verifique se os valores estão em ordem crescente.
crescente = True
numero_anterior = int(input("Digite um numero: "))
valor = 1
while valor != 99999 and crescente:
    valor = int(input("Digite outro numero: "))
    if valor < numero_anterior:
        crescente = False
    numero_anterior = valor    
if crescente:
    print("Ordem crescente! ")
else:
    print("A ordem não esta crescente! ")