q = int(input("Digite o número decimal que deseja converter para binário: "))

result = ''
while q != 0 :
    r =  q % 2
    result = str(r) + result
    q = q // 2
print(result)
