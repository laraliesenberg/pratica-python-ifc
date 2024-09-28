#poligono regular
lado = int(input("Digite o número de lados do polígono:"))
if lado < 3 or lado > 10:
    print("Só aceitamos polígonos de 3 a 10 lados")
elif lado == 3:
    print("O polígono é um triângulo")
elif lado == 4:
    print("O polígono é um quadrilátero")
elif lado == 5:
    print("O polígono é pentágono")
elif lado == 6:
    print("O polígono é um hexagono")
elif lado == 7:
    print ("O polígono é um heptágono")
elif lado == 8:
    print("O polígono é um octógono")
elif lado == 9:
    print ("O polígono é um eneágono")
elif lado == 10:
    print("O polígono é um decágono")