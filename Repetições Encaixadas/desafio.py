# Desafio : Fazer um programa que receba do usuário,que vai digitar uma sequência de números e para cada número que ele digite eu quero que você imprima o fatorial desse número.
n = int(input("Digite um número inteiro: "))
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n=n-1
    print(fatorial)
    n = int(input("Digite um número inteiro: "))