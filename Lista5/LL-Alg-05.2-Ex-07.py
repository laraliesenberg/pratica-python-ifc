def triangulo_3lados(l1, l2, l3):
    if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
        return True
    else:
        return False

def main():
    l1 = float(input("Qual o comprimento do primeiro canudo? "))
    l2 = float(input("Qual o comprimento do segundo canudo? "))
    l3 = float(input("Qual o comprimento do terceiro canudo? "))

    if triangulo_3lados(l1, l2, l3):
        print("O comprimento desses canudos não formam um triângulo")
    else:
        print("O comprimento desses canudos formam um triângulo")
if __name__ == "__main__":
    main()