# 1
# Assumindo que x está definido como um número inteiro, qual expressão booleana abaixo está escrita de forma correta e que sempre retornará True?

True and (4 => 3) #Sintaxe com erro! 
not (x > 0) and (x > 0) #False
(x != 0) and (x == 0) #False
(x > 0) or (x <=0) #True porem pode variar!
(-10 < x < 0) #False

# 2
# Se x = 5 e y = 3, qual será o resultado da expressão abaixo?
x > y
5 > 3
True

# 3 
# Se x = 5, y = 3 e z = 7, qual será o resultado da expressão abaixo?
x > y and x < z
(5 > 3) and (5 < 7)
True

#4
#Qual o resultado do trecho abaixo?
idade=15
maioridade=18
pode_dirigir = idade >= maioridade
pode_dirigir = 15 >= 18
print (pode_dirigir)
False

# 5
# Qual a saída gerada pelo trecho de programa abaixo?
x = 10
y = 15
z = 25
print(x == z - y and z != y - x or not y != z - x)
(10 == 25 - 15) and (25 != 15 - 10) or not (15 != 25 - 10)
(10 == 15) and (25 != 5) or not (15 != 15)
(False and True) or (not False)
False or True
True

# 6
# Considere x = 10, y = 20 e z = 30, assinale quais das alternativas  abaixo resultam em True:

print(not y < 10 or not z == 10)
(not 20 < 10) or (not 30 == 10)
False or True
True

print(not y > 10 or not z > 10)
(not 20 > 10) or (not 30 > 10)
False or False
False

print(x >= 10 or y != z - x)
(10 >= 10) or (20!= 20)
True or False
True

print(x <= 30 and y >= 5)
(10 <= 30) and (20 => 5)
True and True
True

# 7
# Assuma que a = 1 e b = 2. Qual declaração é verdadeira (True)?
not (a == 1)
not (1 == 1)
False

a != 2 or b == 1
(1 != 2) or (2 == 1)
True or False
True

a != 1 or b == 1
(1 != 1) or (2 == 1)
False or False
False

a == 2 and b != 1
(1 == 2) and (2!= 1)
False and True
False