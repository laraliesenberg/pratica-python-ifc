lista = []
lista_nova = []
while True:
    palavra = str(input("Digite uma palavra(enter para parar): "))
    if palavra == "":
        break
    else:
        if not(palavra in lista):
            lista.append(palavra)
print("Palavras distintas:", lista)