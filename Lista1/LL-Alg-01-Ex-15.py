#Área de um polígono regular
import math
l = float(input("Qual o comprimento de um dos lados?"))
n = float(input("Qual o número de lados?"))
numerador = n*(l**2)
pi = math.pi/n
pir = math.radians(pi)
denominador = 4*(math.tan(pir))
area = numerador/denominador
print("A área do polígono regular é", area)