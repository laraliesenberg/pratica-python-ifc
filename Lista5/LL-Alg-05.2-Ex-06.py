def centralizando_string(string, largura):
    centralizando = (largura - len(string)) // 2
    string_centralizada = ' ' * centralizando + string 
    return string_centralizada
    
def main():
    string = input("Digite a string que deseja centralizar: ")
    largura = int(input("Digite a largura da linha: "))
    string_correta = centralizando_string(string, largura)
    print(f'String centralizada: {string_correta}')
    
if __name__ == "__main__":
    main()
