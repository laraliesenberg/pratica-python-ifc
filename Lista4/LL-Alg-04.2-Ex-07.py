soma = 3
i = 1
denominador = 2
print("1- 3")
while i < 15:
    pi = 4 / (denominador * (denominador + 1) * (denominador + 2))
    i = i + 1
    denominador = denominador + 2
    if i % 2 == 0:
        soma = soma + pi 
    else:
        soma = soma - pi
    print(f'{i}- {soma}')
    