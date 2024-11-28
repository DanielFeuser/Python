# Fazer um programa que calcula as raízes de uma equação de segundo grau.
'''import math''' # Importa as funções matemáticas do modulo.
'''math.sqrt(x)''' # Calcula a raiz quadrada de 'x'.
import math
a = float(input("Qual o valor de a? "))
b = float(input("Qual o valor de b? "))
c = float(input("Qual o valor de c? "))
delta = (b ** 2) - 4 * a * c
if delta ==0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("Tera apenas uma raiz:",raiz1)   
elif delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print("A primeira raiz é:",raiz1, "A segunda raiz é:",raiz2)
else:
    print("A equação não tem raizes!")