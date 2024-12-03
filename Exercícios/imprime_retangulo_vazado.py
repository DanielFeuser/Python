#Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
a=altura
while altura > 0:
    n=largura
    print("#",end=(""))
    while largura > 2:
        if altura ==1 or altura ==a:
            print("#",end=(""))
        else:
            print(" ",end=(""))
        largura = largura -1
    print("#",end=(""))
    altura = altura - 1
    largura = n
    print()