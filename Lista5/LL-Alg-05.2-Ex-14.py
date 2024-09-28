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
    
def data_mágica(dia, mes, ano):
    dia_mes = dia * mes
    ultimos_2digitos_ano = ano % 100
    if dia_mes == ultimos_2digitos_ano:
        return True
 
def main():
    for a in range(1901, 2001):
        for m in range(1, 13):
            for d in range(1, dias_em_um_mês(a, m)):
                if data_mágica(d, m, a):
                    print(f'A data {d}/{m}/{a} é mágica')
if __name__ == "__main__":
    main() 