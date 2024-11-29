# Faça um programa que dado um número, ele retorne caso tenha dois números adjacentes iguais.
numero = int(input("Digite um numero: ")) # Pedimos para o usuário informar um número inteiro(int).
adjacentes = False # Como não tenho números adjacentes é falso(False).
banco = numero # Atribuimos o valor da variavel(numero) para a variavel(banco).
while numero != 0 and not adjacentes: # Enquanto a variável(numero) for diferente(!=) de 0 e(and) a variável(adjacentes) não(not) for verdadeira(True).
    resto = numero % 10 # A varíavel(resto) recebe(=) o resto(%) da variável(numero).
    if banco == resto: # Se a variável(banco) for igual(==) a variável(resto).
        adjacentes = True # A variável(adjacentes) de torna verdadeira(True).
    numero = numero // 10 # A variável(numero) vai receber ela mesmo com uma divisão inteira(//) por 10.
    banco = resto # A variável(banco) recebe o valor da variável(resto).
if adjacentes:
    print("Esse numero tem 2 digitos adjacentes: ",banco,"e",resto)
else:
    print("Esse numero não tem numeros adjacentes.")
'''
Meus pensamentos:
1- Nesse programa a gente começa pedindo o numero inteiro para o usuario.
2- Logo depois definimos o valor de adjacentes e banco para poderem entrar no loop. --->Importante deixar banco = numero no começo, pq se colocar um outro numero vai dar errado.
3- Criamos o loop com a condição que o numero não pode ser igual a 0 ou que adjacentes tenha numeros adjacentes.
4- O primeiro comando é criar a variavel(resto) recebendo o valor do resto entre numero % 10.
5- O segundo comando é se banco é igual a resto, caso for igual a variável(adjacentes) passa a ser verdadeira e o loop para.
6- Aqui usei a divisao inteira para retirar o ultimo digito do numero informado pelo usuario.
7- Aqui eu dou o valor de resto para banco, assim armazenando o numero para poder comparar depois.
'''