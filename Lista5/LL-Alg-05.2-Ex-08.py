def letras_maiúsculas(frase):
    frase_correta = ""
    minuscula = True
    for caractere in frase:
        if minuscula and caractere.isalpha():
            frase_correta = frase_correta + caractere.upper()
            minuscula = False
        else:
            frase_correta = frase_correta + caractere
        if caractere == "." or caractere == "!" or caractere == "?":
            minuscula = True
    return frase_correta

def main():
    frase = str(input("Digite uma frase: "))
    corrigida = letras_maiúsculas(frase)
    print(corrigida)
if __name__ == "__main__":
    main()
