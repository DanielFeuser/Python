# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída.
numero = int(input("Digite um número inteiro: "))
soma = 0
while numero > 0:
    resto = numero % 10
    soma = soma + resto
    numero = numero // 10
print(soma)