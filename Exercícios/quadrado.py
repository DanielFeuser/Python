'''
Exercício 1
Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.
Observação: a saída deve estar no formato: "perímetro: x - área: y"
Abaixo um exemplo de como devem ser a entrada e saída de dados do programa:
Exemplo:
Entrada de Dados: 
Digite o valor correspondente ao lado de um quadrado: 3
Saída de Dados:
perímetro: 12 - área: 9
Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez
'''
lado_de_um_quadrado = input("Digite o valor correspondente ao lado de um quadrado: ")
lado = int(lado_de_um_quadrado)
perimetro = lado * 4
area = lado ** 2
print("perímetro:",perimetro,"-","área:",area)