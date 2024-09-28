#idade canina 
idade = int(input("Qual a idade do seu cachorro?"))
if idade < 0:
    print("Não pode números negativos")
elif idade <= 2:
    idade_2 = idade *10.5 
    print("A idade do seu cachorro é:", idade_2)
else: 
    idade_2 = 21 + (idade - 2)*4 
    print("A idade do seu cachorro é:", idade_2)