# Otimizando o codígo de baskara.
import math
a = 2
b = -3
c = -5
delta = (b ** 2) - (4 * a * c)
def raiz1 (a,b):
    return (-b + math.sqrt(delta)) / (2 * a)
def raiz2 (a,b):
    return (-b - math.sqrt(delta)) / (2 * a)

if delta == 0:
    print("a raiz dupla desta equação é X",raiz1(a,b))   
elif delta > 0:
    print("as raízes da equação são",raiz2(a,b),"e",raiz1(a,b))
else:
    print("esta equação não possui raízes reais")
print(delta)