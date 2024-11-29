# Dado um número de cartão de credido diga se o número do cartão de credito aparece na lista ou não

meu_cartao = int(input("Digite o número do seu cartão: ")) # Pedindo o valor inicial para o usuario.
encontrei = False # Ainda não encontrei o cartão, então é False.
cartaoLido = 1 # Sempre adicionar um valor para a variável conseguir entrar no loop.

while cartaoLido !=0 and not encontrei: # Enquanto a variável (cartaLido) for diferente(!=) de 0 e(and) a variável(encontrei) for falsa(False) contia o loop(While).
    cartaoLido = int(input("Digite o numero do proximo cartão: ")) # Usuario tenta encontrar o cartão!.
    if cartaoLido == meu_cartao: # Se(if) o cartão que o usuario tentou acima, for igual(==) ao cartão inicial.
        encontrei = True # a variável(encontrei) se torna verdadeira(True).
if encontrei: # Se(if) a variável(encontrei) for verdadeira(True).
      print("Eba, encontrei meu cartão! ") # imprima.
else: # Caso contrario(Else).
     print("Droga, não encontrei meu cartão") # imprima.