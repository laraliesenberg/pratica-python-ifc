def numeros_ordinais(n):
    if n == 1:
        print(f'Primeiro')
    elif n == 2:
        print(f'Segundo')
    elif n == 3:
        print(f'Terceiro')
    elif n == 4:
        print(f'Quarto')
    elif n == 5:
        print(f'Quinto')
    elif n == 6:
        print(f'Sexto')
    elif n == 7:
        print(f'Sétimo')
    elif n == 8:
        print(f'Oitavo')  
    elif n == 9:
        print(f'Nono')
    elif n == 10:
        print(f'Décimo')
    elif n == 11:
        print(f'Décimo primeiro') 
    elif n == 12:
        print(f'Décimo segundo')

def main():
    n = int(input("Digite um número inteiro(entre 1 e 12): "))
    if n < 1 or n > 12:
        print(" ")
    numeros_ordinais(n)
if __name__ == "__main__":
    main()
    