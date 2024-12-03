def ehprimo(n):
    i = 2
    primo = 1
    while i < n:
        if n % i == 0: # Se o resto da divisão de numero por i for == 0 ele não é primo
            primo = 0
        i = i + 1
    if primo!=0:
        print("primo")
    else:
        print("não primo")


n = int(input("Digite um número inteiro >1:  "))
while n > 1:
    ehprimo(n)
    n = int(input("Digite um número inteiro>1: ")) 