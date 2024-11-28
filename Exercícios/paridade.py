#Par ou ímpar?
'''
Receba um número inteiro na entrada e imprima (par) quando o número for par // (ímpar) quando o número for ímpar.
'''
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0: # Para saber se um número é par, pode verificar se ele é divisível por 2, ou seja, se o resto da divisão for 0.
    print("par")
else:
    print("ímpar")