#ano bissexto
ano = int(input("Digite o ano que deseja saber se é bissexto:"))
if ano % 400 == 0:
    print("O ano é bissexto")
elif ano % 100 == 0:
    print("O ano não é bissexto")
elif ano % 4 == 0:
    print("O ano é bissexto")
else: 
    print("O ano não é bissexto")

