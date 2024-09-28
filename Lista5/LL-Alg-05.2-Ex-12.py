def senha_valida(senha):
    if len(senha) < 8:
        return False
    
    minuscula = False
    maiuscula = False
    numero = False

    for caractere in senha:
        if caractere.islower(): 
            minuscula = True
        elif caractere.isupper():
            maiuscula = True
        elif caractere.isdigit():
            numero = True
    if minuscula and maiuscula and numero:
        return True
    else:
        return False
        
def main():
    senha = input("Digite uma senha: ")
    if senha_valida(senha):
        print("Senha válida")
    else:
        print("Essa senha não é válida")
if __name__ == "__main__":
    main() 
