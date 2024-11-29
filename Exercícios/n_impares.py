#Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.
impar = False
numero = int(input("Digite um número inteiro positivo: "))
valor = 0
i = 0
while i != numero:
    valor = valor + 1
    if valor % 2 != 0:
        impar=True
    else:
        valor= valor + 1
    print(valor)
    i = i + 1