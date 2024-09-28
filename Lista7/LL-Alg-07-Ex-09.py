import random
def sorteio_do_bingo():

    cartela = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}

    while len(cartela['B']) < 5:
        n = random.randint(1, 15)
        if n not in cartela['B']:
            cartela['B'].append(n)
    
    while len(cartela['I']) < 5:
        n = random.randint(16, 30)
        if n not in cartela['I']:
            cartela['I'].append(n)

    while len(cartela['N']) < 5:
        n = random.randint(31, 45)
        if n not in cartela['N']:
            cartela['N'].append(n)

    while len(cartela['G']) < 5:
        n = random.randint(46, 60)
        if n not in cartela['G']:
            cartela['G'].append(n)

    while len(cartela['O']) < 5:
        n = random.randint(61, 75)
        if n not in cartela['O']:
            cartela['O'].append(n)

    return cartela

def cartela_do_bingo(cartela):
    print(" B  |  I  |  N  |  G  |  O  |")
    print("-----------------------------")
    for i in range(5):
        linha = ''
        for letra in 'BINGO':
            linha = linha + f"{cartela[letra][i]:2d}  | "
        print(linha.strip('|'))

def cartela_vencedora(cartela):
    #verificando linhas
    for i in range(5):
        if sum(cartela[letra][i] for letra in 'BINGO') == 0:
            return True
        
    #verificando colunas 
    for letra in 'BINGO':
        if sum(cartela[letra][i] for i in range(5)) == 0:
            return True
            
    #verificando diagonais
    if sum(cartela['BINGO'[i]][i] for i in range(5)) == 0:
        return True
    if sum(cartela['BINGO'[i]][4 - i] for i in range (5)) == 0:
        return True   
    
    return False

def chamando_lista():
    lista = []
    for i in range(1, 76):
        lista.append(i)
    random.shuffle(lista)
    return lista

def anunciar_números(lista, cartela):
    for numero in lista:
        if numero >= 1 and numero <= 15:
            letra = 'B'
        elif numero >= 16 and numero <= 30:
            letra = 'I'
        elif numero >= 31 and numero <= 45:
            letra = 'N'
        elif numero >= 46 and numero <= 60:
            letra = 'G'
        elif numero >= 61 and numero <= 75:
            letra = 'O'

        for i in range(5):
            if cartela[letra][i] == numero:
                cartela[letra][i] = 0
                if cartela_vencedora(cartela):
                    return lista.index(numero) + 1
        
def partidas(n):
    resultados = []
    for _ in range(n):
        cartela = sorteio_do_bingo()
        lista = chamando_lista()
        vitoria = anunciar_números(lista, cartela)
        resultados.append(vitoria)

    minimo = min(resultados)
    maximo = max(resultados)
    media = sum(resultados) / len(resultados)

    return minimo, maximo, media

def main(): 
    numero_de_partidas = 1000
    minimo, maximo, media = partidas(numero_de_partidas)
    print(f"Resultados das {numero_de_partidas} partidas:")
    print(f"Mínimo: {minimo}")
    print(f"Médio: {media:.2f}")
    print(f"Máximo: {maximo}")

if __name__ == "__main__":
    main()