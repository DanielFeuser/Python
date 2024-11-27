'''
#O (or) é bem mais simples de aceitar, apenas depende de um valor ser verdadeiro para ser True.
paitrocinio = False
rolarPromoçao = True
vouAoShow = paitrocinio or rolarPromoçao # Como um valor deu verdadeiro, a resposta é True!
print(vouAoShow)
'''
patrocinio = input("Alguem te deu dinheiro para o show? (sim/não): ")
promocao = input("Conseguiu uma promoção no ingresso? (sim/não): ")
if patrocinio == "sim" or promocao == "sim": # Aqui vemos um exemplo de (or) em um mini programa usando (else e if).
    print("Oba!!! Vamos ao Show!!!")
else:
    print("Fica para a proxima!")