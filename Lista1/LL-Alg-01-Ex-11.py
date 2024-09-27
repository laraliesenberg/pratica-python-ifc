#Distância entre dois pontos na Terra
import math
t1 = float(input("Qual o valor da latitude do primeiro ponto?"))
g1 = float(input("Qual o valor da longitude do primeiro ponto?"))
t2 = float(input("Qual o valor da latitude do segundo ponto?"))
g2 = float(input("Qual o valor da longitude do segundo ponto?"))
t1r = math.radians(t1)
g1r = math.radians(g1)
t2r = math.radians(t2)
g2r = math.radians(g2)
distancia = 6371.01*math.acos(math.sin(t1r)*math.sin(t2r)+math.cos(t1r)*math.cos(t2r)*math.cos(g1r-g2r))
print("A distância entre esses dois pontos ao longo da superficie da Terra é:", distancia)
