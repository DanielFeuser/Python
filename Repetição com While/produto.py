# O produto de uma sequência de números!
tamanho = int(input("Digite o tamanho da sequência de números:"))
produto = 1
i= 0
while i < tamanho: # Enquanto a varíavel (i) for menor que o tamanho digitado pelo usuario, repete.
    valor = int(input("Digite um valor para ser multiplicado: ")) # 1 Aqui o usuario adiciona o número.
    produto = produto * valor # 2 A varíavel (produto) recebe (=) produto * o valor que o usuario forneceu
    i = i + 1 # 3 Soma mais 1 para o valor de i
print("O produto dos valores é:",produto)    