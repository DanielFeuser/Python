'''
# O (not) já é diferente, ambos precisam ser verdadeiros para ser verdadeiros ! ---> se um valor for verdadeiro, passa a ser falso!
# (True + False = False) --- (True + True = True) --- (False + True = False)
sol = input("Está fazendo sol? (sim/não): ")
feriado = input("Vai ser feriado?(sim/não): ")
if not sol == "não" or not feriado == "não" :
    print("Obá, vou para a praia!!!")
else:
    print("Deixa para a proxima!")
'''
# Um exemplo de como o (not) funciona.
sol = input("Está fazendo sol? (sim/não): ")
if not sol == "não":  # 1 -> Caso a resposta do usuario for diferente de não (sim) passa para a proxima parte. Se não (Else) pula para o final do codigo, direto.
    feriado = input("É feriado?(sim/não): ") 
    if not feriado == "não":# 2 -> Caso a resposta do usuario for diferente de não passa para a proxima parte (Perguntar se é feriado)
        print ("Vamos para a praia!!") # 3 -> Caso (feriado = True) Imprime a mensagem "Vamos para a praia!!"
    else:
        print("Não vamos para a praia.") # Se (feriado = False) Imprime a mensagem "Não vamos para a praia."
else:
    print("Não vamos para a praia.") # Se (sol= False) Imprime a mensagem "Não vamos para a praia."