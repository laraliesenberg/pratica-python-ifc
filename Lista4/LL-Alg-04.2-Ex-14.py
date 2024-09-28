n = str(input("Digite o número binário que deseja converter para decimal: "))
tamanho = len(n)

soma_total = 0
for i in range(tamanho):
    if n[i] == "1":
        soma = 2 ** (tamanho - i - 1)
        soma_total = soma_total + soma
    else:
        soma = 0
print(soma_total)
