centavos = int(input("Digite a quantidae de centavos de 0 a 99:"))
moedas50 = centavos//50
resto1 = centavos%50
moedas25 = resto1//25
resto2 = resto1%25
moedas10 = resto2//10
resto3 = resto2%10 
moedas5 = resto3//5
resto4 = resto3%5
moeda1 = resto4//1
print("Moedas de 50 centavos:", moedas50)
print("Moedas de 25 centavos:", moedas25)
print("Moedas de 10 centavos:", moedas10)
print("Moedas de 5 centavos:", moedas5)
print("Moedas de 1 centavo:", moeda1)