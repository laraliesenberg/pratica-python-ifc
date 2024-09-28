n = int(input("Qual a sua matrícula:"))
ano = n//10000
resto = n%10000
semestre = resto//1000


print(f'Foi matriculado no ano:{ano} e no semestre:{semestre}')
