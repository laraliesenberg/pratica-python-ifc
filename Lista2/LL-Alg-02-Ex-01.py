#unidade de tempo
dias = float(input("Digite um intervalo de tempo em dias:"))
horas = float(input("Digite um intervalo de tempo em horas:"))
minutos = float(input("Digite um intervalo de tempo em minutos:"))
segundos = float(input("Digite um intervalo de tempo em segundos:"))
dias_segundos = dias*86400
horas_segundos = horas*3600
minutos_segundos = minutos*60
total = dias_segundos+horas_segundos+minutos_segundos+segundos
print("o total de segundos desse intervalo de tempo é:", total)
