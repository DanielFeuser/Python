# Faça programa que vai lendo do teclado uma sequência de números inteiros terminadas por zero e quando o usuário digita o zero, ele imprimi essa sequência na ordem inversa. Na ordem ao contrário da ordem que o usuário digitou.

numeros=[]
n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))
while n >0:
    numeros.append(n)
    n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))  

i= len(numeros)
a= 0
while i >= 0:
    while a < i:
        a = a + 1
        print(numeros[0-a],end=" ")
    i = i - 1


''' ****melhor resposta****
flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1 
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam - 1
'''