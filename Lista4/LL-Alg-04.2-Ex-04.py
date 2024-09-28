import math

perimetro = 0

x0 = float(input("Digite a coordenada x de um ponto: ")) 
y0 = float(input("Digite a coordenada y de um ponto: ")) 
x_anterior = x0
y_anterior = y0

while True:
    
    x2 = input("Digite a coordenada x de um ponto (enter para sair): ") 
    y2 = input("Digite a coordenada y de um ponto (enter para sair): ") 
    if x2 == ("") or y2 == (""):
        break
    x2 = float(x2)
    y2 = float(y2)

    # calcular distancia p1 ate p2
    d1 = (abs(y2 - y_anterior)**2) + (abs(x2 - x_anterior)**2) 
    d11 = math.sqrt(d1)

    perimetro = perimetro + d11
    # acumular o tamanho deste lado no perimetro total
    x_anterior = x2
    y_anterior = y2
    
    # calcular e acumular a distancia do ultimo ponto para o primeiro (x0, y0)
d2 = (abs(y_anterior - y0)**2) + (abs(x_anterior - x0)**2)
d22 = math.sqrt(d2)
perimetro_total = perimetro + d2
    
print("O perímetro deste polígono é igual a", perimetro_total)