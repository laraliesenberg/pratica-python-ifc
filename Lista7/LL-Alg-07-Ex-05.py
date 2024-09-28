def anagramas(palavra1, palavra2):
    dicionario1 = {}
    dicionario2 = {}
    for caractere in palavra1:
        if caractere in dicionario1:
            dicionario1[caractere] += 1
        else:
            dicionario1[caractere] = 1
    for caractere in palavra2:
        if caractere in dicionario2:
            dicionario2[caractere] += 1
        else:
            dicionario2[caractere] = 1
    if dicionario1 == dicionario2:
        return True
    else:
        return False

def main():
    palavra1 = input("Digite uma palavra: ")
    palavra2 = input("Digite outra palavra: ")
    if anagramas(palavra1, palavra2):
        print("Essas palavras são um anagrama")
    else: 
        print("Essas palavras não são um anagrama")

if __name__ == "__main__":
    main()
