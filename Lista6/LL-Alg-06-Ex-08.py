import re
def somente_palavras(frase):
    frase = re.sub('[!,.?;:()""/]', '', frase)
    frase = frase.strip()
    lista = frase.split()
    return lista


def main():
    frase = str(input("Digite uma frase: "))
    print(somente_palavras(frase))
if __name__ == "__main__":
    main()
