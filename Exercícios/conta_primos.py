#Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

def ehprimo(n):
    i = 2
    primo = 1
    while i < n:
        if n % i == 0: # Se o resto da divisão de numero por i for == 0 ele não é primo
            primo = 0
        i = i + 1
    if primo!=0:
        return True
    else:
        return False




def n_primos(n):
    quantidade = 0
    while n >=2 :
        if ehprimo(n):
            quantidade = quantidade +1
        n = n-1
    return quantidade






n = int(input("Digite um número inteiro >= 2: "))
print(n_primos(n))