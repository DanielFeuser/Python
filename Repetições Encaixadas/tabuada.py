# Tabuada usando Repetições Encaixadas.
coluna = 1
linha = 1
while linha <= 10: # Enquanto linha for menor ou igual a 10...
    while coluna <= 10: # Enquanto coluna for menor ou igual a 10...
        print(linha * coluna, end="\t") # Imprima linha vezes(*) coluna. Esse (end="\t") serve para dar um espaço de tabulação !! poderia usar apenas um (end = "(espaço)") só que ia ficar uma coisa sem padrão.
        coluna = coluna + 1 # Coluna vai receber ela mesmo + 1.
    linha = linha + 1 # Linha vai receber ela mesmo + 1. Logo depois que a primeira condição der o primeiro loop.
    print() # Esse print, serve para pular uma linha entre cada volta.
    coluna = 1 # Aqui defini a coluna novamente para 1, assim podemos passar para o proximo número de linha.