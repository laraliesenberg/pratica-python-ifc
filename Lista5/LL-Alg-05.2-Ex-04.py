def mediana_3_valores(n1, n2, n3):
    x = min(n1, n2, n3)
    y = max(n1, n2, n3)
    meio = (n1 + n2 + n3) - y - x
    print(f'A mediana dos três valores é {meio}')
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = int(input("Digite outro número inteiro: "))
mediana_3_valores(n1, n2, n3)