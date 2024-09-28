n = int(input("Digite um número inteiro positivo:"))

soma = 0
for i in range(1, n+1):
    parcela = (n-(i-1))/i 
    soma = soma + parcela 
print("O valor de A é:", soma)


 