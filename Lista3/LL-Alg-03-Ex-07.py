#níveis de barulho
decibeis = int(input("Digite um nível de volume em decibéis:"))
if decibeis < 40 or decibeis > 130:
    print("Não pode valores menores que 40 e maiores que 130")
elif decibeis == 130:
    print("Esse nível de decibéis equivale ao barulho de uma britadeira")
elif decibeis == 106:
    print("Esse nível de decibéis equivale ao barulho de um cortador de grama")
elif decibeis == 70:
    print("Esse nível de decibéis equivale ao barulho do despertador")
elif decibeis == 40:
    print("Esse nível de decibéis equivale ao barulho de uma sala silenciosa")
elif 130 > decibeis > 106:
    print("O nível está equivalente entre o barulho de uma britadeira e um cortador de grama")
elif 106 > decibeis > 70:
    print("O nível está equivalente entre um cortador de grama e um despertador")
elif 70 > decibeis > 40:
    print("O nível está equivalente entre um despertador e uma sala silenciosa")