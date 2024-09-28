import random
i = 0
lista = []

while i < 6:
    sorteio = random.randint(1,60)
    if sorteio not in lista:
        lista.append(sorteio)
        i = i + 1
    
lista.sort()
print(lista)