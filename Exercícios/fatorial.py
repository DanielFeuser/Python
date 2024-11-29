# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.
numero= int(input("Digite um número inteiro: "))
fatorial = 1
i = 1
while i <= numero:
    fatorial = fatorial * i
    i = i + 1
print(fatorial)