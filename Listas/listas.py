# Listas.
frutas=["banana","maça","uva","kiwi"] # Aqui criamos uma lista com seus devidos valores.
#A Ordem:  0    ,  1  ,   2  ,  3 ----> Sempre começamos a contar do 0.

print(frutas[2]) #Uva

print(frutas[-1]) #Kiwi --> Quando o número é negativo, comaçamos a contar do ultimo iten da lista.

primos=[2,3,5,7,11,13,17,19]
print(len(primos)) # (len) Devolve o número de itens de uma determinada lista/conteiner.

filme =["O que é isso?","Bruno Barreto",1.83,1997]

print(filme[0]) # "O que é isso?"


#Com type podemos verificar a classe/tipo do iten da lista.
print(type(filme[0])) 
print(type(filme[2])) 
print(type(filme[3]))

verduras=[] #Usamos o [] sem nada para definir uma lista vazia.
print(len(verduras)) # Como não tem nada o valor é 0.


verduras.append("batata") # Usamos o (.append()) para adicionar um valor na lista.
print(verduras[0])

frutas[3]= "manga" #Assim que substituimos um valor que já existe na lista por outro.
print(frutas[3])

#Um outro exemplo.
s=[]
s.append(100)
print(s)
s[0] = s[0] +1
print(s)