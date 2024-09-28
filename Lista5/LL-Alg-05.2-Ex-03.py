def calculadora_ecommerce(n):
    if n == 1:
        valor = 10.95
    else:
        valor = 10.95 + 2.95 * (n - 1)
    print(f'Custo do envio: R${valor:.2f}')
n = float(input("Qual a quatidade de itens? "))
calculadora_ecommerce(n)
