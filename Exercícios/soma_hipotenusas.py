# Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.
import math

def é_hipotenusa(n):
    a = 1
    while a < n:
        b = a
        while b < n:
            if n == math.sqrt(a**2 + b**2):
                return True
            b = b + 1
        a = a + 1
    return False

def soma_hipotenusas(n):
    soma = 0
    i = 1  
    while i <= n: 
        if é_hipotenusa(i):  
            soma = soma + i  
        i = i + 1
    return soma
