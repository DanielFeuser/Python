#Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
largura = int(input("Digite um numero"))
altura = int(input("Digite um numero"))
while altura > 0:
    n=largura
    while largura > 0:
        print("#",end=(""))
        largura = largura -1
    altura = altura - 1
    largura = n
    print()