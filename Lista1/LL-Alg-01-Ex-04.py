#area de um terreno
#pedir largura do terreno
largura = float(input("Qual a largura do terreno em metros?"))
#pedir a profundidade do terreno 
profundidade = float(input("Qual a profundidae do terreno em metros?"))
#area em hectares, dividir por 10000
area = largura*profundidade
hectare = area/10000
print("A área do terreno é", hectare, "hectares")