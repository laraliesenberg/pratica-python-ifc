import random

simulacao = 10
total_sorteios = 0

for _ in range(simulacao):
    sorteio = 0
    resultados = []
    while True:
        resultado = random.choice(['A', 'O'])
        resultados.append(resultado)
        print(resultado, end = '')
        sorteio = sorteio + 1
        if len(resultados) >= 3 and resultados[-1] == resultados[-2] == resultados[-3]:
            print(f"({sorteio} sorteios)")
            total_sorteios = total_sorteios + sorteio
            break

media_sorteios = total_sorteios / simulacao
print("Na média, foram necessários", media_sorteios, "sorteios")