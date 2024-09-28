import re
def palindromo(frase):

    def tirando_espaços(frase):
        frase = frase.lower()
        frase = re.sub('[!,.?;:()""/^~]', '', frase)
        frase_completa = ''
        for caractere in frase:
            if caractere in "abcdefghijklmnopqrstuvwxyz":
                frase_completa = frase_completa + caractere
        return frase_completa

    def verificando(frase):
        if len(frase) <= 1:
            return True
        else:
            return frase[0] == frase[-1] and verificando(frase[1: -1])
    return verificando(tirando_espaços(frase))
    
def main():
    frase = input("Digite uma frase para verificar se é palíndromo: ")
    print(palindromo(frase))

if __name__ == "__main__":
    main()