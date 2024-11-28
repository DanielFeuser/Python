
# 1
# Considere a=0, b = 2 e c = 1. O que será impresso pelos comandos abaixo? (Primeiro ajuste corretamente a indentação).
'''
if (a > 0):
    if (b > 0):
        print ("Tudo ok para decolagem!")
    else:
        print ("Tanque principal vazio; voando com combustível reserva!")
else:
    if (c > 0):
        print ("Foguete não tem piloto, mas há outros foguetes disponíveis!") 

a = 0
b = 2
c = 1
if (a > 0): # False.
    if (b > 0): # True, porem como o primeiro if foi False, essa condição não é passada para frente.
        print ("Tudo ok para decolagem!")
    else: # Como o primeiro if foi False, essa condição não é passada para frente.
        print ("Tanque principal vazio; voando com combustível reserva!")
else:
    if (c > 0): # True.
        print ("Foguete não tem piloto, mas há outros foguetes disponíveis!") 

# Ira roldar a condição do else if (c > 0): print ("Foguete não tem piloto, mas há outros foguetes disponíveis!").
'''
# 2
#A legislação de trânsito do Brasil permite que apenas pessoas com no mínimo 18 anos possam habilitar-se para dirigir.Considere que exista uma variável idade e você deverá testar se o usuário pode dirigir ou não e, em seguida, exibir uma mensagem correspondente à sua situação. Todas as opções abaixo dão o resultado correto, porém, qual delas utiliza melhor o recurso do if..else? 

I: if (idade < 18): 
      print ("Não pode tirar carteira de habilitação")
   if (idade >= 18):
      print ("Pode tirar a carteira de habilitação")
      
II: if (idade < 18):  # Essa é a melhor forma!!!!!
       print ("Não pode tirar carteira de habilitação")
    else: 
       print ("Pode tirar a carteira de habilitação")
       
III: if (idade < 18): 
          print (" Não pode tirar carteira de habilitação")
     else: 
         if (idade >= 18): 
               print ("Pode tirar a carteira de habilitação")

IV: if (idade < 18): 
       print ("Não pode tirar carteira de habilitação")
    else: 
      if (idade == 18): 
          print ("Pode tirar a carteira de habilitação")
      else: 
           if (idade > 18): 
               print ("Pode tirar a carteira de habilitação")