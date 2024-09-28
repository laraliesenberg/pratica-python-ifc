frase = input("Digite uma frase: ")
frase = frase.replace(" ", "")
frase = frase.lower()
tamanho = len(frase)
ehpalindromo = True

for i in range(tamanho):
    if frase[i] != frase[tamanho - 1 - i]:
        ehpalindromo = False
        break
if ehpalindromo:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")