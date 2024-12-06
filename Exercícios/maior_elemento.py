#Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.

''''
# Usando o max()


def maior_elemento(lista):
    return max(lista)

lista=[]
n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))
while n >0:
    lista.append(n)
    n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))
print(maior_elemento(lista))
'''

# Manual

def maior_elemento(lista):
    maior=lista[0]
    for numero in lista:
        if numero > maior:
            maior =numero
    return maior        

lista=[]
n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))
while n >0:
    lista.append(n)
    n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))
print(maior_elemento(lista))
