#centena, dezena e unidade
inteiro = int(input("Digite um número inteiro de 3 digitos:"))
centena = inteiro//100
resto1 = inteiro%100
dezena = resto1//10
resto2 = resto1%10
unidade = resto2//1
total = unidade*100 + dezena*10 + centena
print("A ordem inversa do número é:", total)