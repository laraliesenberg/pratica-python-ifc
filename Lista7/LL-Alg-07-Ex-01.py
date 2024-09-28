def caracteres_unicos(palavra):
    letras_vistas = set()
    for letra in palavra:
        if letra in letras_vistas:
            return False
        else:
            letras_vistas.add(letra)
    return True

def main():
    palavra = str(input("Digite uma string: "))
    if caracteres_unicos(palavra):
        print("A string possui caracteres únicos")
    else:
        print("A string possui caracteres repetidos")

if __name__ == "__main__":
    main()
