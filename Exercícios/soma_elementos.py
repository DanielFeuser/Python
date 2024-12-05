#Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.


def soma_elementos(lista):
    soma = 0
    for n in lista:
        soma = soma + n
    return soma


lista=[]
n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))
while n >0:
    lista.append(n)
    n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))
print(soma_elementos(lista))