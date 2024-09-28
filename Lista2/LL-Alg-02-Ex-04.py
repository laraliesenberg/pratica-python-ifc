#ordenação de 3 inteiros
import math
n1 = int(input("Digite um número inteiro:"))
n2 = int(input("Digite outro número inteiro:"))
n3 = int(input("Digite outro número inteiro:"))
x = min(n1,n2,n3)
y = max(n1,n2,n3)
meio = (n1+n2+n3)-y-x
print("A forma ordenada do menor para o maior é", x, meio, y)