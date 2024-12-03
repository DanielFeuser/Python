# Desafio 2 : Separar os loops  em uma função! 
def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n=n-1
    print(fatorial)
n = int(input("Digite um número inteiro: "))
while n >= 0:
    print("O Fatorial de",n,"é:")
    fatorial(n)
    n = int(input("Digite um número inteiro: "))