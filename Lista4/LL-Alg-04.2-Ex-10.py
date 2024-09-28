palavra = input("Digite uma palavra: ")
tamanho = len(palavra)
ehpalindromo = True

for i in range(tamanho):
    if palavra[i] != palavra[tamanho - 1 - i]:
        ehpalindromo = False
        break
if ehpalindromo:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
