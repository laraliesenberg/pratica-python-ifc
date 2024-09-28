def tarifa_taxi(d):
    conversão = d * 1000
    funcao = 4 + 0.25 * (conversão / 140)
    return funcao
    
def main():
    d = float(input("Qual a distância percorrida em KM ? "))
    total = tarifa_taxi(d)
    print(f'O valor da tarifa é R${total:.2f}')
    
if __name__ == "__main__":
    main()