# Um exemplo de ordem de operadores
x = 12312
y = 50
#j = x > 0 and not y == 50 or x + y == 150 # Assim fica complicado de entender a ordem, vamos arrumar !
j= (x > 0) and (not (y ==50)) or (x + y == 150) # Bem melhor !
print(j)