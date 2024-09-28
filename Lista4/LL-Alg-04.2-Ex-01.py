n = int(input("Digite um número inteiro(0 para sair):"))

soma = 0
i = 0

if n == 0:
    print("Erro: O primeiro valor não pode ser 0")
else:
    while n != 0:
        soma = soma + n
        i = i +1
        n = int(input("Digite outro número inteiro:"))
    if i > 0:
        media = soma / i
        print("A média dos valores fornecidos é:", media)
    
