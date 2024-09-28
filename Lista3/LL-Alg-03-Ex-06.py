#classifique o triângulo
l1 = int(input("Digite o comprimento de um dos lados:"))
l2 = int(input("Digite o comprimento do outro lado:"))
l3 = int(input("Digite o comprimento do outro lado:"))
if l1 == l2 == l3:
    print("O triângulo é equilátero")
elif l1 == l2 or l2 == l3 or l1==l3:
    print("O triângulo é isósceles")
elif l1 != l2 != l3:
    print("O triângulo é escaleno")

