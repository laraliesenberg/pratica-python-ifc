def lista_de_divisores(n):
    lista = []
    i = 1
    while i < n:
        if n % i == 0:
            lista.append(i) 
        i = i + 1 
    return sum(lista) == n
      
def main():
    n = 1
    while n <= 10000:
        if lista_de_divisores(n):
            print(n)
        n = n + 1
    
if __name__ == "__main__":
    main() 