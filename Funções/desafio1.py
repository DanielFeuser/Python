# Coeficiente binomial, use as "Funções" para fazer um código mais otimizado.
n= int(input("Digite um número inteiro: "))
k= int(input("Digite outro número inteiro: "))
def fatorial(n):
    fator=1
    while(n>1):
        fator= fator * n
        n= n-1
    return fator
def binomio (n,k):
    return fatorial(n) / (fatorial(k)*(fatorial(n-k)))
print(binomio(n,k))