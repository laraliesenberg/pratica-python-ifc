#Área de um triângulo
import math
l1 = float(input("Qual o comprimento do lado 1?"))
l2 = float(input("Qual o comprimento do lado 2?"))
l3 = float(input("Qual o comprimento do lado 3?"))
l = (l1+l2+l3)/2
area = (l*(l-l1)*(l-l2)*(l-l3))
raiz = math.sqrt(area)
print("A área do triângulo é", raiz)