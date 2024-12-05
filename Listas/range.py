# Comando range.

'''
for iten in range(fim)
    comando

for iten in range(inicio,fim)
    comando

for iten in range(inicio,fim,passo)
    comando    
'''

# Exemplo 1.

for iten in range(20):
    print(iten,end=(" "))
print()

# Exemplo 2.

for iten in range(10,20):
    print(iten ,end=(" "))
print()

# Exemplo 3.

for iten in range(10,20,2):
    print(iten,end=(" "))
print()

# Exemplo 4.

pares = range(0, 40, 2)
for iten in pares:
    print(iten,end=(" "))
print()

# Exemplo 5.

numeros = range(100, 0, -5)
for iten in numeros:
    print(iten,end=(" "))
print()

# Exemplo 6.

pares=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
for i in range(len(pares)):
    pares[i]= pares[i]**3
print(pares,end=(" "))