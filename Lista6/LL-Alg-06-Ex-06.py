def lista_de_divisores(n):
    lista = []
    i = 1
    while i <= n:
        if n % i == 0:
            lista.append(i)  
        i = i + 1  
    return lista

def main():
    n = int(input("Digite um número inteiro: "))
    if True:
        print("Os divisores de", n ,"são", lista_de_divisores(n))

if __name__ == "__main__":
    main() 