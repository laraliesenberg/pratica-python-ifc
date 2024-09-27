#retorno de recicláveis
#pedir a quantidade de vasilhames de um litro ou menos 
vasilhame1 = float(input("Quantos vasilhames de 1L ou menos você tem?"))
#pedir quantidade de vasilhames com mais de um litro
vasilhame2 = float(input("Quantos vailhames com mais de 1L você tem?"))
total = (vasilhame1*0.10) + (vasilhame2*0.25)
print(f'O valor total de créditos é R${total:,.2f}')
