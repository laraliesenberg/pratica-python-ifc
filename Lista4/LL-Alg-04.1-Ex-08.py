i = 0
soma = 0
max = 0
min = 10000 
while i < 10:
    n = int(input("Digite um número inteiro:"))
    i = i + 1 
    soma = soma +n 
    if max < n:
        max = n
    if min > n:
        min = n
print(min)
print(max)
media = soma / 10
print(media)
