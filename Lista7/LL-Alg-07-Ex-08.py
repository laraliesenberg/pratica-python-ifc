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

def main():
    #cartela com linha horizontal
    cartela_1 = sorteio_do_bingo()
    cartela_1['B'][0] = cartela_1['I'][0] = cartela_1['N'][0] = cartela_1['G'][0] = cartela_1['O'][0] = 0

    #cartela com linha vertical
    cartela_2 = sorteio_do_bingo()
    cartela_2['B'][0] = cartela_2['B'][1] = cartela_2['B'][2] = cartela_2['B'][3] = cartela_2['B'][4] = 0

    #cartela com diagonal
    cartela_3 = sorteio_do_bingo()
    cartela_3['B'][0] = cartela_3['I'][1] = cartela_3['N'][2] = cartela_3['G'][3] = cartela_3['O'][4] = 0

    #cartela não vencedora
    cartela_4 = sorteio_do_bingo()
    cartela_4['B'][0] = cartela_4['I'][1] = cartela_4['N'][2] = cartela_4['G'][4] = cartela_4['O'][1] = 0

    for i, cartela in enumerate([cartela_1, cartela_2, cartela_3, cartela_4], 1):
        print(f"Cartela {i}:")
        cartela_do_bingo(cartela)
        if cartela_vencedora(cartela):
            print("\nEsta é uma cartela vencedora!\n")
        else:
            print("\nEsta não é uma cartela vencedora\n")

if __name__ == "__main__":
    main()