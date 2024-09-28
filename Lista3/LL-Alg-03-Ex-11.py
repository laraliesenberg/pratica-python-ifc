#raízes de equação quadrática
import math
a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
c = int(input("Qual o valor de c? "))
if b**2 - 4*a*c < 0:
    print("A equação não possui raízes reais")
elif b**2 - 4*a*c == 0:
    print("A equação tem apenas uma raíz real")
    delta = b**2 - 4*a*c
    raiz_positiva = (((-1)*b) + (math.sqrt(delta))) / (2*a)
    print("A raíz real é", raiz_positiva)
else:
    print("A equação tem duas raízes reais")
    delta = b**2 - 4*a*c
    raiz_positiva = (((-1)*b) + (math.sqrt(delta))) / (2*a)
    raiz_negativa = (((-1)*b) - (math.sqrt(delta))) / (2*a)
    print(f'As duas raízes reais são, {raiz_positiva, raiz_negativa}')
print(delta)
