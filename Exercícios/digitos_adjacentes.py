#Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".
numero = int(input("Digite um número inteiro: "))
adjacentes = 1819849818498494654894616135186
total = False

while numero > 0:
    resto = numero % 10
    if resto == adjacentes:
        total = True
    numero = numero // 10
    adjacentes = resto
if total:
    print("sim")
else:
    print("não")