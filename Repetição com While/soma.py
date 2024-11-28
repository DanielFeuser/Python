# Soma de uma sequência de números.
print("Caso queira parar de somar digite 0")
soma = 0
valor = 1
while valor !=0:
    valor = int(input("Digite um número para ser somado: "))
    soma = soma + valor
print("A soma dos números é:",soma)