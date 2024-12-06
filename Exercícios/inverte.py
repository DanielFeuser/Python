#Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.



lista=[]
n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))
while n >0:
    lista.append(n)
    n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))


copia=lista[::-1]
for n in copia:
    print(n)