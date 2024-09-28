numero = int(input("Digite um número interio (maior ou igual a 2): "))
fator = 2
n = numero

if numero < 2:
    print("Erro")
while fator <= numero:
    if n % fator == 0:
        n = n / fator
        print(fator)
    else:
        fator = fator + 1


