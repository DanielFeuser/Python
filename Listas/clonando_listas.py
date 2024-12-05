# Clonando listas.
'''
lista1[:] => Devolve um clone da lista.
'''
lista1=[1,2,3,4,5,6,7,8,9,10]

lista2=lista1[:]

print (lista1)
print (lista2)

lista2.append(11)

print (lista1)
print (lista2) # Como foi clonado, não altera o valor da lista 1