x = float(input("Digite o número que deseja calcular a raiz quadrada: "))
raiz = x / 2
while abs(raiz * raiz - x) < 10 ** -12:
    raiz = (raiz + x / raiz) / 2
print("O valor aproximado da raiz quadrada de", x ,"é", raiz)