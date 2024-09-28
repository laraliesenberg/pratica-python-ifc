def dias_em_um_mês(mes, ano):
    
    if mes == 4 or mes == 6 or mes == 7 or mes == 11:
        return 30
    if mes == 2:
        if ano % 400 == 0:
            return 29
        elif ano % 100 == 0:
            return 28
        elif ano % 4 == 0:
            return 29
        else:
            return 28
    else:
        return 31

def main():
    mes = int(input("Digite um mês: "))
    ano = int(input("Digite um ano: "))

    dia = dias_em_um_mês(mes, ano)
    print("Esse mês tem {:d} dias".format(dia))
if __name__ == "__main__":
    main()