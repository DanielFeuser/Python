# Faça um programa que verifique se os valores estão em ordem decrescente.
decrescente = True
anterior = int(input("Digite um valor: ")) # Pedimos um primeiro valor para o usuário.
valor = 1 
while valor != 0 and decrescente: # Condição: Se o valor for diferente(!=) de 0 e(and) a variável(decrescente) for verdadeira(True) continuar com o loop.
    valor = int(input("Digite outro valor: ")) # Pedimos para o usuário um novo valor!
    if valor > anterior: # Caso o valor que o usuário passou for maior(>).
        decrescente = False # Transforma a variável(decrescente) em falso(False).
    anterior = valor # Atribui um novo valor para o número anterior do usuário.
if decrescente: # Caso os valores passados pelo usuário estejam em ordem decrescente imprima a mensagem (Consegui, está em ordem decrescente :))
    print("Consegui, está em ordem decrescente :) ")
else:
    print("Droga, não está em ordem decrescente :( ") # Caso os valores passados pelo usuário não estejam em ordem decrescente imprima a mensagem (Droga, não está em ordem decrescente :()