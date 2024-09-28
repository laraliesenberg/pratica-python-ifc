n = int(input("Digite uma data no formato DDMMAA:"))
d1 = n//10000
resto = n%10000
m1 = resto//100
a1 = resto%100
print(d1, m1, a1)

data = a1*10000 + m1*100 +d1
print("O resultado da inversão da data é:", data)
