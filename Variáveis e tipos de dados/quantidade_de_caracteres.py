#Como armazenar em uma nova variável a quantidade total de caracteres de três variáveis?
cumprimento = "Olá"
nome = "Ana"
turno = "bom dia"
tamanho =len(cumprimento) + len(nome) + len(turno) #Opção longa
print(tamanho)
''' Opção pratica 
tamanho = cumprimento + nome + turno
print (len(tamanho))
'''