#Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.


def remove_repetidos(lista):
    copia = []  # Nova lista para armazenar os elementos sem repetição
    for item in lista:
        if item not in copia:  # Só adiciona se ainda não estiver na nova lista
            copia.append(item)
    return (sorted(copia))  # Ordena a lista resultante e imprime

# Lista de exemplo
lista=[]
n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))
while n >0:
    lista.append(n)
    n= int(input("Digite uma sequência de números inteiros terminadas por 0: "))
print(remove_repetidos(lista))