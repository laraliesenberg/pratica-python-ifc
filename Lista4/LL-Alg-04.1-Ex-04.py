n = int(input("Digite um número inteiro positivo:"))

soma = 0
for i in range(1, n+1):
    # montar uma parcela e acumular a parcela no valor total
    parcela = 1/i
    soma = soma + parcela
print("O valor de A é:", soma)
