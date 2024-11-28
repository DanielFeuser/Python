# Distância entre dois pontos.
# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima (longe) na saída. Caso o contrário, quando a distância for menor que 10, imprima (perto).
import math
num1 = float(input("Digite um número: ")) #Xa.
num2 = float(input("Digite um número: ")) #Ya.
num3 = float(input("Digite um número: ")) #Xb.
num4 = float(input("Digite um número: ")) #Yb.
distancia = math.sqrt((num3 - num1)**2 + (num4 - num2)**2)
if distancia >= 10:
    print("longe")
else:
    print("perto")