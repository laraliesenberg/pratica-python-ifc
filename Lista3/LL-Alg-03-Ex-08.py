#nota para frequência
nota = str(input("Digite uma nota:"))
oitava = int(input("Digite a oitava da nota:"))

if oitava < 0 or oitava > 8:
    print("Não pode números a baixo de 0 e a cima de 8")
else:
    if nota == "C":
        frequencia = 261.63
    elif nota == "D":
        frequencia = 293.66
    elif nota == "E":
        frequencia = 329.63
    elif nota == "F":
        frequencia = 349.23 
    elif nota == "G":
        frequencia = 392.00 
    elif nota == "A":
        frequencia = 440.00 
    elif nota == "B":
        frequencia = 493.88
    frequencia_final = frequencia /2**(4 - oitava)
    print("A frequencia dessa nota é", frequencia_final) 
