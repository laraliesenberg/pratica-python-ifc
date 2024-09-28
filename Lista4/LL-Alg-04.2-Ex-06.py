bits = 0
while True:
    bits = str(input("Digite uma sequência de 8 bits: "))
    if bits == (""):
        break
    elif len(bits) != 8 :
        print("Erro")
    elif bits.count("1") % 2 == 0:
        print("O bit de paridade é 0")
    else:
        print("O bit de paridade é 1")
