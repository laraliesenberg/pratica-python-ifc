i = 0
soma = 0
max = 0
min = 10000 
while True:
    resposta = input("Digite um número inteiro:")
    if resposta == (""):
        break
    n = int(resposta)
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