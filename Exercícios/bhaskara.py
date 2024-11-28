# Desafio da videoaula.

#escreva um programa que calcula as raízes de uma equação do segundo grau.

#Quando não houver raízes reais imprima: esta equação não possui raízes reais
#Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima: a raiz desta equação é X
#Quando houver duas raízes reais imprima: as raízes da equação são X e Y
#Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente.
import math
a = float(input("Qual o valor de a? "))
b = float(input("Qual o valor de b? "))
c = float(input("Qual o valor de c? "))
delta = (b ** 2) - 4 * a * c
if delta ==0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz dupla desta equação é X",raiz1)   
elif delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    if raiz1 < raiz2:
        print("as raízes da equação são",raiz1,"e",raiz2)
    else:
        print("as raízes da equação são",raiz2,"e",raiz1)
else:
    print("esta equação não possui raízes reais")