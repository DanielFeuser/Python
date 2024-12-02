#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
import math
def eh_primo(x):
    if x == 2:
        return True
    i = b = 2
    while i <= math.sqrt(x):
        if x % i == 0: # Se o resto da divisão de numero por i for == 0 ele não é primo
            b = 1
        i = i + 1
    if b == 1:
        return False
    else:
        return True

def maior_primo(x):
    if eh_primo(x) == True:
        return x
    while eh_primo(x) == False:
        x = x - 1
    return x