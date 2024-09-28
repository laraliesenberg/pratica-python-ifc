#soma dos digitos de um inteiro
import math 
n1 = int(input("Digite um número inteiro de 4 digitos:"))
a = n1//1000
resto1 = n1%1000
b = resto1//100
resto2 = resto1%100
c = resto2//10
resto3 = resto2%10
total = (a+b+c+resto3)
print("A soma dos 4 digitos é:", total)