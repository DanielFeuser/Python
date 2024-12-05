# Adicionando uma lista no final de outra lista.

"""
[1,2]+[3,4]
[1,2,3,4,]
"""

print([1,2,3]+[4,5,6])
print()

a=[10,20,30]
b=[40,50,60]

print(a+b)
print()

print(a+b+b+a)
print()

#A concatenação gera uma nova lista, sem alterar as listas. existentes.

b = a + [5]

print(b)
print(a)