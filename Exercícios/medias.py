'''
Exercício 2
Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:
Exemplo:
Entrada de Dados:
Digite a primeira nota: 4
Digite a segunda nota: 5
Digite a terceira nota: 6
Digite a quarta nota: 7
Saída de Dados:
A média aritmética é 5.5
Dica: uso do print
Quando você usa o comando print para imprimir mais de uma coisa, ele inclui automaticamente espaços entre os argumentos impressos. Cuidado para não incluir espaços demais na sua resposta! O corretor perceberá e tirará pontos
>>>print("uma coisa", "outra coisa")
uma coisa outra coisa
>>>print("aqui tem ", 2, "espaços")
aqui tem  2 espaços
'''
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))
quarta_nota = float(input("Digite a quarta nota: "))
media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4
print("A média aritmética é ",media)