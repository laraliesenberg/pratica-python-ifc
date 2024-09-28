i = 0
while True:
    idade = input("Digite a idade do visitante (digite enter parar finalizar): ")
    if idade == (""):
        break
    n = int(idade)
    if n <= 2:
        valor = 0
    elif n >= 3 and n <= 12:
        valor = 14
    elif n >= 65:
        valor = 18
    else:
        valor = 23
    i = i + valor
    valor_total = i
print(f'O preço total é R${valor_total:.2f}')