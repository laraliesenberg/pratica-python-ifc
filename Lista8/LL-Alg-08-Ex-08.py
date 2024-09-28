def binário_recursiva(q):
    if q == 0:
        return "0"
    elif q == 1:
        return "1"
    else: 
        r = q % 2
        digitos = binário_recursiva(q // 2)
        return  digitos + str(r) 

def main():
    q = int(input("Digite um número decimal(não pode ser negativo): "))
    binario = binário_recursiva(q)
    print(f'O número binário do número decimal {q} é {binario}')

if __name__ == "__main__":
    main()