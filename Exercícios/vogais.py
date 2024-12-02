# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

def vogal (x):
    if x.lower() in ["a", "e", "i", "o", "u"]: # lower() Converte toda a string para letras minúsculas antes da comparação.
        #in ["a", "e", "i", "o", "u"]: Usa uma lista para verificar se o caractere está entre as vogais. Essa abordagem torna o código mais legível e compacto.
        return True
    else:
        return False
