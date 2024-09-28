#centena, dezena e unidade
inteiro = int(input("Digite um número inteiro de 3 digitos:"))
centena1 = inteiro//100
resto1 = inteiro%100
centena_total = centena1*100
dezena1 = resto1//10
resto2 = resto1%10
dezena_total = dezena1*10
unidade = resto2//1
print("Centena:", centena_total, "Dezena:", dezena_total, "Unidade:", unidade )
