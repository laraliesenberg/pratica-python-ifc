
i = 0
soma = 4.95
while soma <= 24.95:
    preco_original = soma
    valor_desconto = (preco_original * 0.60)
    desconto_aplicado = (preco_original - valor_desconto)
    soma = soma + 5
    i = i + 1
    print(f"R${preco_original:.2f}\t\tR${valor_desconto:.2f}\t\tR${desconto_aplicado:.2f}\t\t")
