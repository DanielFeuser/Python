# Construa um programa que calcule a soma dos digitos de um número. Exemplo: 12 --> 1 + 2 = 3.
# Dica: Divisão inteira(//) e resto(%).
#Exemplo:
''' 
x = 6532
x % 10 = 2
x // 10 = 653
''' 
# Fazer um laço(while) que sempre pegue o último digito e some em uma varíavel. Depois que somar descartar o número.

numero = int(input("Digite um valor: "))
soma = 0
while numero > 0: # Enquanto o numero for maior que 0 continue a repetição.
    resto = numero % 10 # Usamos o Resto para pegar o último digito do valor.
    soma = soma + resto # Aqui somamos o ultimo digito com a variavel(soma), assim armazenando o seu valor.
    numero = numero // 10 # Aqui descartamos o ultimo numero que foi usado na condição de cima.
print("A soma dos digitos é :",soma)