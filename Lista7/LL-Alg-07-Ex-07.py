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

def main():
    cartela = sorteio_do_bingo()
    cartela_do_bingo(cartela)

if __name__ == "__main__":
    main()