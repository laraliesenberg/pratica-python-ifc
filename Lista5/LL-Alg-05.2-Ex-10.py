def números_primos(n):
    while True:
        i = 2
        resultado = True
        if n == 1:
            return False
        while i < n:
            if n % i == 0:
                resultado = False
            i = i + 1
        return resultado

def main():
    n = int(input("Digite um número inteiro: "))
    if números_primos(n):
        print(f'{n} é um número primo')
    else:
        print(f'{n} não é um número primo')
        
if __name__ == "__main__":
    main()