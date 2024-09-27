#conta do almoço
#pedir preço do prato principal
pp = float(input("Qual o preço do prato principal?"))
#pedir preço do suco
suco = float(input("Qual o preço do suco?"))
#pedir preço da sobremesa
sobremesa = float(input("Qual o preço da sobremesa?"))
soma = pp+suco+sobremesa
taxadeservico = soma*0.10
total = soma+taxadeservico
print(f'O valor total da conta deu R${total:,.2f}')
