#juros compostos
#perguntar valor inicial depositado na conta
valor_inicial = float(input("Qual foi o valor depositado inicialmente em sua conta?"))
apos1ano = valor_inicial*0.12
total1 = valor_inicial+apos1ano
print(f'O saldo da conta após 1 ano é R${total1:,.2f}')
apos2anos = total1*0.12
total2 = total1+apos2anos
print(f'O saldo da conta após 2 anos é R${total2:,.2f}')
apos3anos = total2*0.12
total3 = total2+apos3anos
print(f'O saldo da conta após 3 anos é R${total3:,.2f}')

