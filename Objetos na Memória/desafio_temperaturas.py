#Dada uma lista contendo as temperaturas médias registradas em cada dia de um determinado mês, desenvolva um programa em Python que determine a temperatura mínima e a temperatura máxima do mês.

def MinMax():
    print("A menor temperatura desse mês foi: ", minima(temperaturas), "C.")
    print("A maior temperatuda desse mês foi: ", maxima(temperaturas), "C.")

def minima(temps):
    min=temps[0]
    i=1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i= i +1
    return min

def maxima(temps):
    max=temps[0]
    i=1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i= i +1
    return max





temperaturas=[18, 20, 22, 21, 19, 23, 25, 26, 24, 22, 20, 21, 19, 18, 22, 25, 26, 24, 23, 21, 19, 18, 22, 24, 26, 25, 23, 21, 19, 20, 22]
MinMax()