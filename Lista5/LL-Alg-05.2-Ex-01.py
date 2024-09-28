import math
def hipotenusa(a, b):
    cateto_1 = a ** 2
    cateto_2 = b ** 2
    hipotenusa = math.sqrt(cateto_1 + cateto_2)
    return hipotenusa
a = float(input("Digite o comprimento do menor lado do triângulo: "))
b = float(input("Digite o comprimento do outro menor lado do triângulo: "))
print(hipotenusa(a, b))
