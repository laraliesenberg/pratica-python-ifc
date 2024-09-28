def anagramas_frase(frase1, frase2):
    frase1 = frase1.upper()
    frase2 = frase2.upper()
    frase1 = frase1.replace(" ", "")
    frase2 = frase2.replace(" ", "")
    dicionario1 = {}
    dicionario2 = {}
    for caractere in frase1:
        if caractere in dicionario1:
            dicionario1[caractere] += 1
        else:
            dicionario1[caractere] = 1
    for caractere in frase2:
        if caractere in dicionario2:
            dicionario2[caractere] += 1
        else:
            dicionario2[caractere] = 1
    if dicionario1 == dicionario2:
        return True
    else:
        return False

def main():
    frase1 = input("Digite uma frase: ")
    frase2 = input("Digite outra frase: ")
    if anagramas_frase(frase1, frase2):
        print("Essas frases são um anagrama")
    else: 
        print("Essas frases não são um anagrama")

if __name__ == "__main__":
    main()