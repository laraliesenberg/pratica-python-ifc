import random
def sorteia_dado():
    i = 0
    lista = []
    while i < 1000000:
        n = random.randint(1,6)
        lista.append(n) 
        i = i + 1
    quantidade_1 = lista.count(1)
    quantidade_2 = lista.count(2)
    quantidade_3 = lista.count(3)
    quantidade_4 = lista.count(4)
    quantidade_5 = lista.count(5)
    quantidade_6 = lista.count(6)

    #Calculando probabilidade 
    prob_1 = 100 * quantidade_1 / 1000000
    prob_2 = 100 * quantidade_2 / 1000000
    prob_3 = 100 * quantidade_3 / 1000000
    prob_4 = 100 * quantidade_4 / 1000000
    prob_5 = 100 * quantidade_5 / 1000000
    prob_6 = 100 * quantidade_6 / 1000000

    #Imprimindo 
    print("Quantas vezes cada número caiu e a probabilidade: ")
    print(f'1- {quantidade_1} - {prob_1:.2f}%')
    print(f'2- {quantidade_2} - {prob_2:.2f}%')
    print(f'3- {quantidade_3} - {prob_3:.2f}%')
    print(f'4- {quantidade_4} - {prob_4:.2f}%')
    print(f'5- {quantidade_5} - {prob_5:.2f}%')
    print(f'6- {quantidade_6} - {prob_6:.2f}%')
sorteia_dado()